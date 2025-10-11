from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart')  # Goes to cart page

def cart_view(request):
    cart_items = CartItem.objects.all()
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


# Create your views here.
