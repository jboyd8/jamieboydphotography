from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):
    """
     Renders the cart contents page.
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """
     Adds the amount of a selected product to the cart
    """
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id] + quantity)
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    messages.success(request, 'You have successfully added an item to your cart.')
    return redirect(reverse('store'))


def adjust_cart(request, id):
    """
    Adjust the quantity of a specified product
    """
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
