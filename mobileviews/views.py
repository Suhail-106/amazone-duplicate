from django.shortcuts import render, get_object_or_404, redirect
from mobileviews.models import mainob, cartItemMobile, bestseller
from maincontainer.models import CartItem

def add_to_cart_mobile(request, mobile_id):
    producob = get_object_or_404(mainob, id=mobile_id)

    matched_nameofperse = producob.name
    matched_price = float(producob.startingprice)

    if matched_nameofperse is None:
        return redirect('home')
    
    cart_item, created = cartItemMobile.objects.get_or_create(
        content = matched_nameofperse,
        price = matched_price,
        defaults={'off174':0, 'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')    

def cart_view_mobile(request):
    mobile_cart_items = cartItemMobile.objects.all()
    general_cart_items = CartItem.objects.all()
    allmainob = mainob.objects.all()
    allbestseller = bestseller.objects.all()

    mobile_total_price = 0
    general_total_price = 0
    mobile_total_quantity = 0
    general_total_quantity = 0

    for item in mobile_cart_items:
        mobile_total_price += item.price * item.quantity
        mobile_total_quantity += item.quantity

    for item in general_cart_items:
        general_total_price += item.price * item.quantity
        general_total_quantity += item.quantity

    return render(request, 'cart1.html', {
        'mobile_cart_items': mobile_cart_items,
        'general_cart_items': general_cart_items,
        'mobile_total_price': mobile_total_price,
        'general_total_price': general_total_price,
        'mobile_cart_count': mobile_total_quantity,
        'general_cart_count': general_total_quantity,
        'mainob': allmainob,
        'bestseller': allbestseller,
    })


def product_view(request):
    return render(request, 'product_list.html')


def footermobile_view(request):
    cart_items = CartItem.objects.all()
    cart_itemsmobile = cartItemMobile.objects.all()
    
    total_quantity = sum(item.quantity for item in cart_items)
    mobile_cart_count = sum(item.quantity for item in cart_itemsmobile)
    
    return render(request, 'footermobile.html', {
        'cart_count': total_quantity,
        'mobile_cart_count': mobile_cart_count,
        'testing_variable': 'this is working'  # just for testing
    })