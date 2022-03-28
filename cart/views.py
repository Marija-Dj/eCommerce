from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from product.models import Product


# Create your views here.

from  .cart import Cart

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'product/summary.html', {'cart':cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        cart_qty = cart.__len__()
        response = JsonResponse({'qty':cart_qty})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

    cart_qty = cart.__len__()
    cart_total = cart.get_total_price()
    response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total})
    return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'subtotal': cart_total})
        return response
