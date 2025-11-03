from django.shortcuts import render, get_object_or_404, redirect
from Fashion.models import vocalforlocal, vocalforlocal1, vocalforlocal2, shopclothing, shopfootwear, Budget_Add_Ons,shopBeauty
from maincontainer.models import CartItem
from django.http import HttpResponse
from decimal import Decimal,InvalidOperation


def vocalforlocal13(request):
    allvocalforloacal = vocalforlocal.objects.all()
    allvocalforloacal2 = vocalforlocal2.objects.all()
    allvocalforloacal1 = vocalforlocal1.objects.all()
    allshopclothing = shopclothing.objects.all()
    allshopfootwear = shopfootwear.objects.all()
    allBudgetaddons = Budget_Add_Ons.objects.all()
    allshopbeauty = shopBeauty.objects.all()
   
    return render(request,'fashion.html',{
    'vocalforlocal':allvocalforloacal,
    'vocalforlocal1':allvocalforloacal1,
    'vocalforlocal2':allvocalforloacal2,
    'shopclothing':allshopclothing,
    'shopfootwear':allshopfootwear,
    'Budgetaddons':allBudgetaddons,
    'shopbeauty':allshopbeauty,
    })

def vocalforlocal1_addtocart(request,vocalforlocalid):
    vocal = get_object_or_404(vocalforlocal,id=vocalforlocalid)
    
    pricevocal = vocal.price
    offervocal = vocal.offer
    intrestingvocal = vocal.interestincontent 

    if intrestingvocal is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingvocal,
        price = pricevocal,
        off174 = offervocal,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))    

def product_details_vocalforlocal1(request, vocalforlocal1_id):
    product = get_object_or_404(vocalforlocal, id=vocalforlocal1_id)
    price = Decimal(product.price)
    offer = Decimal(product.offer)
    final_pricevocalforlocal1 = price - (price * offer / Decimal(100))

    return render(request, 'product_detail1.html', {'vocalforlocal1_product': product, 'type': 'vocalforlocal1',
   'final_pricevocalforlocal1':final_pricevocalforlocal1,'type':'vocalforlocal1'})


def buy_now_vocalforlocal1(request, vocalforlocal1_id):
    # Get product from electronicsstored model
    product = get_object_or_404(vocalforlocal, id=vocalforlocal1_id)

    # Extract values from model
    name = product.interestincontent
    price = Decimal(product.price)
    offer = Decimal(product.offer)
    image = product.image

    extra_offer = request.GET.get('extra_offer', 'false') == 'true'

    if extra_offer:
        # Add extra 10% discount
        offer += Decimal(10)
    # Calculate final discounted price
    final_price = price - (price * offer / Decimal(100))

      #for send details for product user------
    request.session['product_name'] = name
    request.session['product_price'] = str(price)
    request.session['product_offer'] = str(offer)
    request.session['product_final_price'] = str(final_price)
 

    # Render template
    return render(request, "buy_now1.html", {
        "product": product,
        "name": name,
        "price": price,
        "offer": offer,
        "final_price": final_price.quantize(Decimal('0.01')),
        "image": image
    })
   


#---------------------------------------end of vocalforlocal1----------------------------------------------



#----------------------------------------------vocalforlocal2-----------------------------------------------

def vocalforlocal2_addtocart(request,vocalforlocalid2):
    vocal1 = get_object_or_404(vocalforlocal1,id=vocalforlocalid2)
    
    pricevocal1 = vocal1.price1
    offervocal1 = vocal1.offer1
    intrestingvocal1 = vocal1.interestincontent1 

    if intrestingvocal1 is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingvocal1,
        price = pricevocal1,
        off174 = offervocal1,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))   

def product_details_vocalforlocal2(request, vocalforlocal2_id):
    product = get_object_or_404(vocalforlocal1, id=vocalforlocal2_id)
    price = Decimal(product.price1)
    offer = Decimal(product.offer1)
    final_pricevocalforlocal2 = price - (price * offer / Decimal(100))

    return render(request, 'product_detail1.html', {'vocalforlocal2_product': product, 'type': 'vocalforlocal2',
   'final_pricevocalforlocal2':final_pricevocalforlocal2,'type':'vocalforlocal2'})


def buy_now_vocalforlocal2(request, vocalforlocal2_id):
    # Get product from electronicsstored model
    product = get_object_or_404(vocalforlocal1, id=vocalforlocal2_id)

    # Extract values from model
    name = product.interestincontent1
    price = Decimal(product.price1)
    offer = Decimal(product.offer1)
    image = product.image1

    extra_offer = request.GET.get('extra_offer', 'false') == 'true'

    if extra_offer:
        # Add extra 10% discount
        offer += Decimal(10)
    # Calculate final discounted price
    final_price = price - (price * offer / Decimal(100))

      #for send details for product user------
    request.session['product_name'] = name
    request.session['product_price'] = str(price)
    request.session['product_offer'] = str(offer)
    request.session['product_final_price'] = str(final_price)


    # Render template
    return render(request, "buy_now1.html", {
        "product": product,
        "name": name,
        "price": price,
        "offer": offer,
        "final_price": final_price.quantize(Decimal('0.01')),
        "image": image
    })  


#------------------------------------------------end for vocalforlocal2----------------------------------------------



#--------------------------------------shop clothings-------------------------------------------------------------

def shopclothing_addtocart(request,shopclothingsid):
    shopclo = get_object_or_404(shopclothing,id=shopclothingsid)
    
    priceshopclo = shopclo.priceshopclothing 
    intrestingshopclo = shopclo.contentshopclothing 

    if intrestingshopclo is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopclo,
        price = priceshopclo,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))  


def product_details_shopclothing(request, shopclothing_id):
    product = get_object_or_404(shopclothing, id=shopclothing_id)
    return render(request, 'product_detailsbedroom.html', {'shopclothing_product': product, 'type': 'shopclothing'})


def buy_now_shopclothing(request, shopclothing_id):
    # Get product from electronicsstored model
    product = get_object_or_404(shopclothing, id=shopclothing_id)
    
    # Extract values safely
    name = product.contentshopclothing or "Unknown Product"
    image = product.imageshopclothing

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.priceshopclothing)
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
        "image": image
    })  



#-------------------------------------------------end Shop clothing-----------------------------------------


#----------------------------------------------shopfootwear-------------------------------------


def shopfootwear_addtocart(request,shopfootwearid):
    shopfoot = get_object_or_404(shopfootwear,id=shopfootwearid)
    
    priceshopfoot = shopfoot.priceshopfootwear 
    intrestingshopfoot = shopfoot.contentshopfootwear 

    if intrestingshopfoot is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopfoot,
        price = priceshopfoot,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))   

def product_details_shopfootwear(request, shopfootwear_id):
    product = get_object_or_404(shopfootwear, id=shopfootwear_id)
    return render(request, 'product_detailsbedroom.html', {'shopfootwear_product': product, 'type': 'shopfootwear'})


def buy_now_shopfootwear(request, shopfootwear_id):
    # Get product from electronicsstored model
    product = get_object_or_404(shopfootwear, id=shopfootwear_id)

  # Extract values safely
    name = product.contentshopfootwear or "Unknown Product"
    image = product.imageshopfootwear

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.priceshopfootwear)
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
        "image": image
    })  

#----------------------------------------end shopfootwear---------------------------------------------

#----------------------------------------------Shop Budget_add-----------------------------

def shopBudget_addtocart(request,shopBudgetid):
    shopBudget = get_object_or_404(Budget_Add_Ons,id=shopBudgetid)
    
    priceshopBudget = shopBudget.priceshopBudget
    intrestingshopBudget = shopBudget.contentshopBudget 

    if intrestingshopBudget is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopBudget,
        price = priceshopBudget,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))  

def product_details_shopBudget(request, shopBudget_id):
    product = get_object_or_404(Budget_Add_Ons, id=shopBudget_id)
    return render(request, 'product_detailsbedroom.html', {'shopBudget_product': product, 'type': 'shopBudget'})


def buy_now_shopBudget(request, shopBudget_id):
    # Get product from electronicsstored model
    product = get_object_or_404(Budget_Add_Ons, id=shopBudget_id)

   # Extract values safely
    name = product.contentshopBudget or "Unknown Product"
    image = product.imageshopBudget

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.priceshopBudget)
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
        "image": image
    })  

#------------------------------------------------end of budghet_ads_ons----------------------------------------

#-----------------------------------------shopbeauty----------------------------------------------------------------

def shopbeauty_addtocart(request,shopbeautyid):
    shopbeauty = get_object_or_404(shopBeauty,id=shopbeautyid)
    
    priceshopbeauty = shopbeauty.priceshopBeauty
    intrestingshopbeauty = shopbeauty.contentshopBeauty 

    if intrestingshopbeauty is None:
        return redirect('vocalforlocal')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = intrestingshopbeauty,
        price = priceshopbeauty,
        off174 = 0,
        defaults={'quantity':1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','vocalforlocal'))    

def product_details_shopbeauty(request, shopbeauty_id):
    product = get_object_or_404(shopBeauty, id=shopbeauty_id)
    return render(request, 'product_detailsbedroom.html', {'shopbeauty_product': product, 'type': 'shopbeauty'})


def buy_now_shopbeauty(request, shopbeauty_id):
    # Get product from electronicsstored model
    product = get_object_or_404(shopBeauty, id=shopbeauty_id)

    # Extract values safely
    name = product.contentshopBeauty or "Unknown Product"
    image = product.imageshopBeauty

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.priceshopBeauty)
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
        "image": image
    }) 


#----------------------------------end shopbeauty-----------------------------------------------------

def product_details(request, type, id):
    model_map = {
        "shopbeauty": shopBeauty,
        "shopBudget": Budget_Add_Ons,
        "shopfootwear": shopfootwear,
        "shopclothing": shopclothing,
    }

    model = model_map.get(type)
    if not model:
        return HttpResponse("Invalid product type")

    product = get_object_or_404(model, id=id)

    # auto detect karega correct field name
    image_field = next((f.name for f in model._meta.fields if "image" in f.name), None)
    content_field = next((f.name for f in model._meta.fields if "content" in f.name), None)
    price_field = next((f.name for f in model._meta.fields if "price" in f.name), None)

    context = {
        "name12": getattr(product, content_field, ""),
        "price12": getattr(product, price_field, ""),
        "images12": getattr(product, image_field, ""),
    }

    return render(request, "product_detail1.html", context)
