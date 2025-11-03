from django.shortcuts import render, get_object_or_404, redirect
from mobileviews.models import mainob, cartItemMobile, bestseller
from maincontainer.models import CartItem
from decimal import Decimal,InvalidOperation

def add_to_cart_mainob(request, mainob_id):
    producob = get_object_or_404(mainob, id=mainob_id)

    matched_nameofperse = producob.name
    matched_price = float(producob.startingprice)

    if matched_nameofperse is None:
        return redirect('home')
    
    cart_item, created = CartItem.objects.get_or_create(
        content = matched_nameofperse,
        price = matched_price,
        defaults={'off174':0, 'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER','home'))    


def product_details_mainob(request, mainob_id):
    product = get_object_or_404(mainob, id=mainob_id)
    return render(request, 'product_detailsbedroom.html', {'mainob_product': product, 'type': 'mainob'})


def buy_now_mainob(request, mainob_id):
    # Get product from electronicsstored model
    product = get_object_or_404(mainob, id=mainob_id)

    name = product.name or "Unknown Product"
    image = product.image

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.startingprice)
    except (InvalidOperation, TypeError, ValueError):
        price = Decimal(0)

    # ✅ Offer safe handling
    try:
        offer = Decimal(getattr(product, "offer", 0) or 0)
    except (InvalidOperation, TypeError, ValueError):
        offer = Decimal(0)

    # ✅ Final price calculation
    if offer > 0:
        final_price = price - (price * offer / Decimal(100))
    else:
        final_price = price

    # ✅ Save clean values in session
    request.session['product_name'] = name
    request.session['product_price'] = str(price.quantize(Decimal('0.01')))
    request.session['product_offer'] = str(offer.quantize(Decimal('0.01')))
    request.session['product_final_price'] = str(final_price.quantize(Decimal('0.01')))

    # ✅ Optional: store user email for order
    if request.user.is_authenticated:
        request.session['user_email'] = request.user.email
    # Render template
    return render(request, "buy_now1.html", {
        "product": product,
        "name": name,
        "price": price,
        "final_price": final_price.quantize(Decimal('0.01')),
        "image": image
    })
#----------------------------------------------end of mainob-------------------------------------------------

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