from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    if request.method == 'POST':
        if product_id in request.session['cart']:
            request.session['cart'][product_id] += 1
        else:
            request.session['cart'][product_id] = 1

    return render(request, 'cart/cart.html', product_id)

def remove_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        if product_id in request.session['cart']:
            request.session['cart'][product_id] -= 1
            if request.session['cart'][product_id] == 0:
                del request.session['cart'][product_id]
    return render(request, 'cart/cart.html')

def remove_single_item_from_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        if product_id in request.session['cart']:
            del request.session['cart'][product_id]
    return render(request, 'cart/cart.html')
