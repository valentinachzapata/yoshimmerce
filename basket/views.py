from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from basket.basket import Basket
from yoshistore.models import Product



def carrito_summary(request):
    basket = Basket(request)
    print(basket)
    return render(request, 'carrito.html', { 'basket' : basket })

def carrito_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        print(basketqty)
        response = JsonResponse({ 'qty' : basketqty })
        return response