from django.shortcuts import render, get_object_or_404,redirect
from HomeandKitchen.models import bedroom
from maincontainer.models import CartItem
from decimal import Decimal, InvalidOperation

def homekitchen(request):
    allbedroom = bedroom.objects.all()
    return render(request,'home&kitchen.html',{'bedroom':allbedroom})

def bedroomaddtocart(request,bedroomid):
    bedroom1 = get_object_or_404(bedroom, id=bedroomid)

    bedroomcontent = bedroom1.content
    bedroomprice = bedroom1.price

    if bedroomcontent is None:
        return redirect('home&kitchen')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        off174 = 0,
        price = bedroomprice,
        content = bedroomcontent,
        defaults={'quantity':1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','home%kitchen')) 

def product_details_bedroom(request, bedroom_id):
    product = get_object_or_404(bedroom, id=bedroom_id)
    return render(request, 'product_detailsbedroom.html', {'bedroom_product': product, 'type': 'bedroom'})


def buy_now_bedroom(request, bedroom_id):
    # Get product from bedroom model
    product = get_object_or_404(bedroom, id=bedroom_id)

    # Extract values safely
    name = product.content or "Unknown Product"
    image = product.image

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.price)
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

    # ✅ Render template
    return render(request, "buy_now1.html", {
        "product": product,
        "name": name,
        "price": price,
        "offer": offer,
        "final_price": final_price,
        "image": image,
    }) 



# Create your views here.
