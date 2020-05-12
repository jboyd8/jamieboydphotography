from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from store.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """
    If method is GET, should display empty forms. If POST, should pick up the details from both the order form and
    the payment form. Additionally should pick up the cart items. Added error handling to catch exceptions when the
    payment id processed. Flash relevant messages one the payment is either processed or rejected.
    """
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            except Exception as e:
                messages.error(request, "Your card was declined, you weren't charged.")

            if customer.paid:
                messages.success(request, 'You have successfully paid')
                request.session['cart'] = {}
                return redirect(reverse('store'))
            else:
                messages.error(request, 'Unable to take payment')
        else:
            print(payment_form.errors)
            messages.error(request, 'We were unable to take payment with that card!')
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

        context = {
            'order_form': order_form,
            'payment_form': payment_form,
            'publishable': settings.STRIPE_PUBLISHABLE
        }
        return render(request, 'checkout/checkout.html', context)
