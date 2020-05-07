from django.shortcuts import render, redirect, reverse


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
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request):
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
