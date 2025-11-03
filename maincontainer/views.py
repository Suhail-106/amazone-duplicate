from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from maincontainer.models import main,Profile,UserAddress,datasave, actiontoys, electronicsstored, electronicsheadphones, CartItem, mobile, electronicslaptop, Fresh, mainmobile, product as ProductModel
from django.db.models import Sum
from mobileviews.models import mainob, cartItemMobile, mainob2, mainob3, bestseller
from Fashion.models import vocalforlocal, vocalforlocal1, vocalforlocal2, shopclothing, shopfootwear,Budget_Add_Ons,shopBeauty
from datetime import date
from HomeandKitchen.models import bedroom
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout,authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.utils.encoding import force_str
from decimal import Decimal, InvalidOperation


def get_discounted(price,off):
    return round(price - (price * off / 100), 2)

def homepage(request):
    allcontain = main.objects.all()
    allproduct = ProductModel.objects.all()
    allactiontoys = actiontoys.objects.all()
    allmobile = mobile.objects.all()
    for mob in allmobile:
        mob.final_price = get_discounted(mob.mrpmobile, mob.offermobile)    

    if request.method == "GET":
      st = request.GET.get("searchbar")
      if st!= None:
          allcontain = main.objects.filter(heading2__icontains=st)
          allproduct = ProductModel.objects.filter(
               Q(content1__icontains=st) |
               Q(content2__icontains=st) |
               Q(content3__icontains=st) |
               Q(content4__icontains=st)
          )
          allmobile = mobile.objects.filter(nameofmobile__icontains=st)
    
    matched_data = bestseller.objects.all()
    allfresh = Fresh.objects.all()
    for product in allproduct:
        product.final_price1 = get_discounted(product.price1, product.off171)
        product.final_price2 = get_discounted(product.price2, product.off172)
        product.final_price3 = get_discounted(product.price3, product.off173)
        product.final_price4 = get_discounted(product.price4, product.off174)
     
    allmainob = mainob.objects.all()
    allmainob2 = mainob2.objects.all()
    allmainob3 = mainob3.objects.all()

    cart_count = CartItem.objects.aggregate(total_qty=Sum('quantity'))['total_qty'] or 0 
   #mobile_cart_count = cartItemMobile.objects.aggregate(total_qty=Sum('quantity'))['total_qty'] or 0

    #fashion for 430px ke neeche
    allvocalforloacal = vocalforlocal.objects.all()
    allvocalforloacal2 = vocalforlocal2.objects.all()
    allvocalforloacal1 = vocalforlocal1.objects.all()
    allshopclothing = shopclothing.objects.all()
    allshopfootwear = shopfootwear.objects.all()
    allBudgetaddons = Budget_Add_Ons.objects.all()
    allshopbeauty = shopBeauty.objects.all()

    #electronics 
    allelectronicslaptop = electronicslaptop.objects.all()
    allelectronicsheadphones = electronicsheadphones.objects.all()
    allelectronicsstored = electronicsstored.objects.all()
    allmainmobile = mainmobile.objects.all()

    for mainmobiles in allmainmobile:
        mainmobiles.final_price = get_discounted(mainmobiles.mainmmrp,mainmobiles.mainmoffer)

    for stored in allelectronicsstored:
        stored.final_pricestored = get_discounted(stored.storedmrpprice, stored.storedoffer)

    for laptop in allelectronicslaptop:
        laptop.final_price = get_discounted(laptop.laptopmrpprice, laptop.laptopoffer)

    for headphones in allelectronicsheadphones:
        headphones.final_priceheadphones = get_discounted(headphones.headphonesmrpprice, headphones.headphonesoffer)
    
    # condition for pincode 
  
    return render(request, 'index.html', {
        'page_obj': allcontain,
        'product':allproduct,
        'cart_count':cart_count,
        'actiontoys':allactiontoys,
        'mobile':allmobile,
        'mainob':allmainob,
       # 'mobile_cart_count':mobile_cart_count,
        'mainob2':allmainob2,
        'mainob3':allmainob3,
        'matched_data': matched_data,
        'fresh':allfresh,
        'vocalforlocal':allvocalforloacal,
        'vocalforlocal1':allvocalforloacal1,
        'vocalforlocal2':allvocalforloacal2,
        'shopclothing':allshopclothing,
        'shopfootwear':allshopfootwear,
        'electronicslaptop':allelectronicslaptop,
        'electronicsheadphones':allelectronicsheadphones,
        'electronicsstored':allelectronicsstored,
        'Budgetaddons':allBudgetaddons,
        'shopbeauty':allshopbeauty,
        'mainmobile':allmainmobile
        })


# views.py
def add_to_cart(request, product_id, which_content):
    product_obj = get_object_or_404(ProductModel, id=product_id)
    
    matched_content = None
    matched_price = None
    matched_offer = None

    for i in range(1, 5):
        content = getattr(product_obj, f"content{i}")
        price = getattr(product_obj, f"price{i}")
        offer = getattr(product_obj, f"off17{i}")
        if content == which_content:
            matched_content = content
            matched_price = price
            matched_offer = offer
            break

    if matched_content is None:
        return redirect('home')  # Safety check

    cart_item, created = CartItem.objects.get_or_create(
        product=product_obj,
        content=matched_content,
        defaults={'price': matched_price, 'off174':matched_offer, 'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','home'))


#----------------------------------------------home mobile modls.py -------------------

def add_to_cartmobile(request, mobile_id):
    homemobile = get_object_or_404(mobile,id=mobile_id)

    nameofhomemobile = homemobile. nameofmobile
    homemobileoffer = homemobile.offermobile
    homemobileprice = homemobile.mrpmobile

    if nameofhomemobile is None:
        return redirect('home')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = nameofhomemobile,
        price = homemobileprice,
        defaults={'quantity':1,'off174':homemobileoffer}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','home'))    


def product_details_viewelectronicsmobile(request, mobile_id):
    product = get_object_or_404(mobile, id=mobile_id)
    price = Decimal(product.mrpmobile)
    offer = Decimal(product.offermobile)
    final_pricemobile = round(price - (price * offer / Decimal(100)),2)

    return render(request, 'product_detail1.html', {'mobile_product': product, 'type': 'mobile',
    'final_pricemobile':final_pricemobile,'type':'mobile'})


def buy_now_mobile(request, mobile_id):
    # Get product from electronicsstored model
    product = get_object_or_404(mobile, id=mobile_id)

    # Extract values from model
    name = product.nameofmobile
    price = Decimal(product.mrpmobile)
    offer = Decimal(product.offermobile)
    image = product.imagemobile

    extra_offer = request.GET.get('extra_offer', 'false') == 'true'

    if extra_offer:
        # Add extra 10% discount
        offer += Decimal(10)

    # Calculate final discounted price
    final_price = price - (price * offer / Decimal(100))

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

#---------------------------end of home mobile models.py ----------------------    

def cart_view(request):
    cart_items = CartItem.objects.all()
    allproduct = ProductModel.objects.all()
    allmobile = mobile.objects.all()
    allbestseller = bestseller.objects.all()
    allfresh = Fresh.objects.all
    allmainmobile = mainmobile.objects.all()
    allelectronicslaptop = electronicslaptop.objects.all()
    allelectronicsheadphones = electronicsheadphones.objects.all()
    allvocalforloacal = vocalforlocal.objects.all()
    allvocalforloacal1 = vocalforlocal1.objects.all()
    allshopclothing = shopclothing.objects.all()
    allshopfootwear = shopfootwear.objects.all()
    allbudgetaddons = Budget_Add_Ons.objects.all()
    allShopBeauty = shopBeauty.objects.all() 
    allbedroom = bedroom.objects.all()
    allmainob = mainob.objects.all()
   
    total_price = 0
    total_offer = 0
    total_offer_percentage = 0
    total_price_total = 0
    total_quantity = 0

    for item in cart_items:
        discount_amount =  item.price * item.off174/100
        total_offer += discount_amount * item.quantity
        total_prices = item.price - (item.price * item.off174/100)
        total_price += total_prices * item.quantity 
        total_price_total += item.price * item.quantity 
        total_quantity += item.quantity

        total_offer_percentage = round((total_offer / total_price_total) * 100,2)

    return render(request, 'cart.html', {
        'cart_items': cart_items, 'product': allproduct,'total_price': total_price,
        'total_offer': total_offer, 'total_offer_percentage':total_offer_percentage,'mobile': allmobile, 
        'cart_count':total_quantity, 'bestseller':allbestseller, 'fresh': allfresh,'mainmobile':allmainmobile,
        'electronicslaptop':allelectronicslaptop,'electronicsheadphones':allelectronicsheadphones, 'vocalforlocal':allvocalforloacal,
        'vocalforlocal1':allvocalforloacal1,'shopclothing':allshopclothing,
        'shopfootwear':allshopfootwear, 'Budgetaddons':allbudgetaddons, 'shopBeauty':allShopBeauty, 'bedroom':allbedroom,
        'mainob':allmainob,
        
    })


#--------------------------------------------bestseller watch-------------------------------------

def filtered_products1(request, bestseller_id):
    best = get_object_or_404(bestseller, id=bestseller_id)  # ✅ different variable name

    nameofbestseller = best.contentm
    bestsellerprice = best.pricewacth

    if nameofbestseller is None:
        return redirect('filtered_products')

    cart_item, created = CartItem.objects.get_or_create(
        product=None,
        content=nameofbestseller,
        price=bestsellerprice,
        defaults={'quantity': 1,'off174':0}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', 'filtered_products'))


def product_details_bestseller(request, bestseller_id):
    product = get_object_or_404(bestseller, id=bestseller_id)
    return render(request, 'product_detail1.html', {'bestseller_product': product, 'type': 'bestseller',})


def buy_now_bestseller(request, bestseller_id):
    # Get product from electronicsstored model
    product = get_object_or_404(bestseller, id=bestseller_id)

    name = product.contentm or "Unknown Product"
    image = product.Imagem

    # ✅ Safe decimal conversion for price
    try:
        price = Decimal(product.pricewacth)
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
   

def filtered_products(request):
    matched_data = bestseller.objects.all()
   
    cart_count = CartItem.objects.aggregate(total_qty=Sum('quantity'))['total_qty'] or 0 
    
    return render(request, 'product_list.html', {'matched_data': matched_data,'cart_count':cart_count})





#----------------------------------------------end of bestseller of watch--------------------------------


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

#--------------------------------------Fresh vegetables------------------------------------------

def fresh(request):
    allfresh = Fresh.objects.all()
    return render(request, 'fresh.html',{'fresh':allfresh})

def fresh_addtocart(request, fresh_id):
    fresh = get_object_or_404(Fresh,id=fresh_id)

    nameoffresh = fresh.nameoffresh
    freshoffer = fresh.offerfresh
    freshprice = fresh.pricefresh

    if nameoffresh is None:
        return redirect('fresh')
     
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = nameoffresh,
        price = freshprice,
        defaults={'quantity':1,'off174':freshoffer}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','fresh'))    


def product_details_viewelectronicsfresh(request, fresh_id):
    product = get_object_or_404(Fresh, id=fresh_id)
    price = Decimal(product.pricefresh)
    offer = Decimal(product.offerfresh)
    final_pricefresh = price - (price * offer / Decimal(100))

    return render(request, 'product_detail1.html', {'fresh_product': product, 'type': 'fresh',
   'final_pricefresh':final_pricefresh,'type':'fresh'})


def buy_now_fresh(request, fresh_id):
    # Get product from electronicsstored model
    product = get_object_or_404(Fresh, id=fresh_id)

    # Extract values from model
    name = product.nameoffresh
    price = Decimal(product.pricefresh)
    offer = Decimal(product.offerfresh)
    image = product.vegitablebimagefresh

    extra_offer = request.GET.get('extra_offer', 'false') == 'true'

    if extra_offer:
        # Add extra 10% discount
        offer += Decimal(10)
    # Calculate final discounted price
    final_price = price - (price * offer / Decimal(100))

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
   

#------------------------------------------------end of Fresh vegetables---------------------------------------------


#----------------------------------------------------mobile page -----------------------------------------------------

 

def mobilepage(request):
    today = date.today()
    allmainmobiles = mainmobile.objects.all()
    allmobile = mobile.objects.all()
    for mob in allmobile:
        mob.final_price = get_discounted(mob.mrpmobile, mob.offermobile)   
        
    for mainmobiles in allmainmobiles:
        mainmobiles.final_price = get_discounted(mainmobiles.mainmmrp,mainmobiles.mainmoffer)
    return render(request, 'mobile.html',
    {'mainmobile':allmainmobiles,'today':today,'mobile':allmobile})

def mainmobileaddtocart(request, mainmobile_id):
    mainmobile1 = get_object_or_404(mainmobile, id=mainmobile_id)

    nameofmainmobile = mainmobile1.nameofmmobile
    specsofmaincamera = mainmobile1.specsofcamera
    specsofmaindurability = mainmobile1.specsofdurability
    mainmrpprice = mainmobile1.mainmprice
    mainmobileoffer = mainmobile1.mainmoffer

    if nameofmainmobile is None:
        return redirect('mobile')
    
    content_combined = f"{nameofmainmobile} | Camera: {specsofmaincamera} | Durability: {specsofmaindurability}"
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = content_combined,
        price = mainmrpprice,
        defaults={'quantity':1, 'off174':mainmobileoffer}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','mobile'))    

def buy_now_mobilepage(request, mobilepage_id):
    # Get product from electronicsstored model
    product = get_object_or_404(mainmobile, id=mobilepage_id)

    # Extract values from model
    name = product.nameofmmobile
    price = Decimal(product.mainmprice)
    offer = Decimal(product.mainmoffer)
    image = product.mainimagemobile
     
    extra_offer = request.GET.get('extra_offer', 'false') == 'true'

    if extra_offer:
        # Add extra 10% discount
        offer += Decimal(10)
    # Calculate final discounted price
    final_price = price - (price * offer / Decimal(100))

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

def product_details_mobilepage(request, mobilepage_id):
    product = get_object_or_404(mainmobile, id=mobilepage_id)
    price = Decimal(product.mainmprice)
    offer = Decimal(product.mainmoffer)
    final_pricemobilepage = price - (price * offer / Decimal(100))

    return render(request, 'product_detail1.html', {'mobilepage_product': product, 'type': 'mobilepage',
   'final_pricemobilepage':final_pricemobilepage,'type':'mobilepage'})

#---------------------------------------------end of mobile page ----------------------------------------

#----------------------------electronics laptop-------------------------------------

def laptopaddtocart(request, laptop_id):
    ellaptop = get_object_or_404(electronicslaptop,id=laptop_id)

    nameofelectronicslaptop = ellaptop.laptopname
    electronicslaptopoffer = ellaptop.laptopoffer
    electronicslaptopmrpprice = ellaptop.laptopmrpprice

    if nameofelectronicslaptop is None:
        return redirect('electronics')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = nameofelectronicslaptop,
        price = electronicslaptopmrpprice,
        defaults={'quantity':1,'off174':electronicslaptopoffer}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','electronics'))    

#-----------------------------------------electronics page ----------------------------------------------------
def electronics(request):
    allelectronicslaptop = electronicslaptop.objects.all()
    allelectronicsheadphones = electronicsheadphones.objects.all()
    allelectronicsstored = electronicsstored.objects.all()

    for stored in allelectronicsstored:
        stored.final_pricestored = get_discounted(stored.storedmrpprice, stored.storedoffer)

    for laptop in allelectronicslaptop:
        laptop.final_price = get_discounted(laptop.laptopmrpprice, laptop.laptopoffer)

    for headphones in allelectronicsheadphones:
        headphones.final_priceheadphones = get_discounted(headphones.headphonesmrpprice, headphones.headphonesoffer)

    return render(request,'electronics.html',
    {
    'electronicslaptop':allelectronicslaptop,
    'electronicsheadphones':allelectronicsheadphones,
    'electronicsstored':allelectronicsstored,
    })

def product_details_viewelectronicslaptop(request, laptop_id):
    product = get_object_or_404(electronicslaptop, id=laptop_id)
    price = Decimal(product.laptopmrpprice)
    offer = Decimal(product.laptopoffer)
    final_pricelaptop = price - (price * offer / Decimal(100))
    return render(request, 'product_detail1.html', {'laptop_product': product, 'type': 'laptop',
    'final_pricelaptop':final_pricelaptop,'type':'laptop'})

def buy_now_laptop(request, laptop_id):
    # Get product from electronicsstored model
    product = get_object_or_404(electronicslaptop, id=laptop_id)

    # Extract values from model
    name = product.laptopname
    price = Decimal(product.laptopmrpprice)
    offer = Decimal(product.laptopoffer)
    image = product.laptopimage
     
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


#-------------------------------------------------------------electronics headphones-----------------------------------


def headphonesaddtocart(request, headphones_id):
    elheadphones = get_object_or_404(electronicsheadphones,id=headphones_id)

    nameofelectronicsheadphones = elheadphones.headphonesname
    electronicsheadphonesoffer = elheadphones.headphonesoffer
    electronicsheadphonesmrpprice = elheadphones.headphonesmrpprice

    if nameofelectronicsheadphones is None:
        return redirect('electronics')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = nameofelectronicsheadphones,
        price = electronicsheadphonesmrpprice,
        defaults={'quantity':1,'off174':electronicsheadphonesoffer}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','electronics'))    


def product_details_viewelectronicsheadphones(request, headphones_id):
    product = get_object_or_404(electronicsheadphones, id=headphones_id)
    price = Decimal(product.headphonesmrpprice)
    offer = Decimal(product.headphonesoffer)
    final_priceheadphones = price - (price * offer / Decimal(100))
    return render(request, 'product_detail1.html', {'headphones_product': product, 'type': 'headphones',
    'final_priceheadphones':final_priceheadphones,'type':'headphones'})


def buy_now_headphones(request, headphones_id):
    # Get product from electronicsstored model
    product = get_object_or_404(electronicsheadphones, id=headphones_id)

    # Extract values from model
    name = product.headphonesname
    price = Decimal(product.headphonesmrpprice)
    offer = Decimal(product.headphonesoffer)
    image = product.headphonesimage

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


#-------------------------------------------------------electronics stored function -------------------------------------
def storedaddtocart(request, stored_id):
    product = get_object_or_404(electronicsstored, id=stored_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=None,  # since this is from electronicsstored, not main product model
        content=product.storedname,
        price=product.storedmrpprice,
        defaults={'quantity': 1, 'off174': product.storedoffer}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','electronics'))    
    # apne cart view ka name lagao

def product_details_viewelectronicsstored(request, stored_id):
    product = get_object_or_404(electronicsstored, id=stored_id)
    price = Decimal(product.storedmrpprice)
    offer = Decimal(product.storedoffer)
    final_pricestored = price - (price * offer / Decimal(100))
    return render(request, 'product_detail1.html', {'stored_product': product, 'type': 'stored',
    'final_pricestored':final_pricestored,'type':'stored'})

def buy_now_stored(request, stored_id):
    # Get product from electronicsstored model
    product = get_object_or_404(electronicsstored, id=stored_id)

    # Extract values from model
    name = product.storedname
    price = Decimal(product.storedmrpprice)
    offer = Decimal(product.storedoffer)
    image = product.storedimage

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

#-------------------------------------------------------end of electronics stored----------------------------------------------------

#------------------------------------------------------------universal add to cart -----------------------------------------------


def autoupdatedataandimage(request):
    return render(request,'autoupdatedataandimage.html')    

def form(request):
    return render(request,'form.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmedPassword = request.POST.get('confirmpassword')

        if password != confirmedPassword:
            return render(request,'register.html')
    
        if User.objects.filter(username = username).exists():
           return render(request,'register.html', {'error':'User name already exist'})
        if User.objects.filter(email = email).exists():
            return render(request, 'register.html',{'error':'email already exist'})
        
        user = User.objects.create(
            username = username, email = email)
        
        user.set_password(password)   # hash password
        user.save()
        Profile.objects.create(user = user)
        
        #extra save
        datasave.objects.create(
            username = username,
            email = email,
            password = password,
            confirmpassword = confirmedPassword
        )
        return redirect('login')
    return render(request,'register.html')

def user_login(request):   # apna function ka naam user_login rakho, clash avoid hoga 
    error_massage = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['user_email'] = email
       
        password = request.POST.get('password')

        if not email or not password:
            error_massage = '⚠️ Please fill all your details'
            return render(request, 'login.html',{'error_massage':error_massage})

        user = None
        if User.objects.filter(username=email).exists():
            user = User.objects.get(username=email)
        elif User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)   
        else:
            error_massage = '⚠️ User not found. Please check your input.'
            return render(request, 'login.html',{'error_massage':error_massage})

        user_auth = authenticate(request, username=user.username, password=password)

        if user_auth is None:
            error_massage = '⚠️ Invalid password.'
            return render(request, 'login.html', {'error_massage':error_massage})
        
        login(request, user_auth)

        otp = random.randint(100000,999999)
        
        request.session['otp'] = str(otp)
        request.session['email'] = user.email
        request.session['username'] = user.username

        send_mail(
            subject = 'Your otp code',
            message = f'Hello {user.username},\nYour otp code is: {otp}',
            from_email = 'companypvtltd35@gmail.com',
            recipient_list = [user.email],
        )
        time.sleep(3)
        return redirect('verify_otp')

    return render(request, "login.html",{'error_massage':error_massage})
    
def verify_otp(request):
    error_message = ''
    username = request.session.get('username') 

    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')
        datasave.objects.update(
            user_otp=user_otp, 
            session_otp=session_otp
        )

        if user_otp == session_otp:
            del request.session['otp']
            return redirect('home')
        else:
            error_message = '❌ Invalid OTP. Please try again.'
    return render(request, 'verify_otp.html', {'error_message': error_message})




def product_detail(request, product_id, which_content):
    product = get_object_or_404(ProductModel, id=product_id)
    
    selected_image = None
    selected_content = None
    selected_price = None
    selected_offer = None
    final_price = None  # <-- New field

    for i in range(1, 5):
        content = getattr(product, f"content{i}")
        if content == which_content:
            selected_image = getattr(product, f"image{i}")
            selected_content = content
            selected_price = getattr(product, f"price{i}")
            selected_offer = getattr(product, f"off17{i}")
            
            # ✅ Calculate final price (if offer exists)
            try:
                price = Decimal(selected_price)
                offer = Decimal(selected_offer)
                final_price = price - (price * offer / Decimal(100))
            except:
                final_price = selected_price  # fallback if invalid data
            break

    context = {
        'product': product,
        'image': selected_image,
        'content': selected_content,
        'price': selected_price,
        'offer': selected_offer,
        'finalprice': round(final_price, 2) if final_price else None,  # ✅ added field
    }

    return render(request, 'product_detail.html', context)




def buy_now(request, product_id, which_content):
    product_item = get_object_or_404(ProductModel, id=product_id)
    
    selected_image = None
    selected_content = None
    selected_price = None
    selected_offer = None

    # ✅ Find which content user selected
    for i in range(1, 5):
        content = getattr(product_item, f"content{i}")
        if content == which_content:
            selected_image = getattr(product_item, f"image{i}")
            selected_content = content
            selected_price = getattr(product_item, f"price{i}")
            selected_offer = getattr(product_item, f"off17{i}", None)
            break

    # 🧠 Handle price safely
    base_price = Decimal(selected_price or 0)

    # 🧠 Handle offer (if missing → 0)
    try:
        discount = Decimal(selected_offer or 0)
    except (ValueError, TypeError):
        discount = Decimal(0)

    # 🧮 Calculate final price (if offer > 0)
    if discount > 0:
        final_price = base_price - (base_price * discount / Decimal(100))
    else:
        final_price = base_price

    # ✅ Save values in session (for add_address1)
    request.session['product_name'] = selected_content or product_item.product_name or "Unknown Product"
    request.session['product_price'] = str(base_price)
    request.session['product_offer'] = str(discount)
    request.session['product_final_price'] = str(final_price.quantize(Decimal('0.01')))

    # 👇 Optional: store email if user logged in
    if request.user.is_authenticated:
        request.session['user_email'] = request.user.email

    # 🧾 Render the Buy Now page
    return render(request, "buy_now.html", {
        "product": product_item,
        "image": selected_image,
        "content": selected_content,
        "price": base_price,
        "discount": discount,
        "final_price": final_price.quantize(Decimal('0.01')),
    })


def payment_success(request):
    return render(request, "payment_success.html")



def dashboard(requst):
    pass

def logout(request):
    pass


    
@login_required(login_url='login')
def add_address(request):
    if request.method == "POST":
        name = request.POST.get("name")
        street = request.POST.get("street")
        area = request.POST.get("area")
        landmark = request.POST.get("landmark")
        full_address = request.POST.get("full_address")
        Address1 = request.POST.get("Address1")

        # 🧠 Get product details from session
        product_name = request.session.get('product_name', 'Unknown Product')
        product_price = request.session.get('product_price', 'N/A')
        product_offer = request.session.get('product_offer', '0')
        product_final_price = request.session.get('product_final_price', 'N/A')
        email = request.user.email or request.session.get('user_email')

        # 🧮 Offer value
        try:
            offer_value = float(product_offer)
        except (ValueError, TypeError):
            offer_value = 0.0

        # 🧾 Create text for mail
        if offer_value > 0:
            user_price_section = f"MRP: ₹{product_price}\nDiscount: {product_offer}%\nFinal Price: ₹{product_final_price}"
            admin_price_section = f"Price: ₹{product_price}\nOffer: {product_offer}%\nFinal Price: ₹{product_final_price}"
        else:
            user_price_section = f"Price: ₹{product_price}"
            admin_price_section = f"Price: ₹{product_price}"

        # 💾 Save Address
        UserAddress.objects.create(
            name=name,
            street=street,
            area=area,
            landmark=landmark,
            full_address=full_address,
            address=Address1,
        )

        # 📧 Admin email
        admin_message = f"""
NEW ORDER RECEIVED

Name: {name}
Street: {street}
Area: {area}
Landmark: {landmark}
Full Address: {full_address}
Current Address: {Address1}

Product: {product_name}
{admin_price_section}
"""

        # 📧 User email
        user_message = f"""
Hello {name},

Your order has been confirmed!

Product: {product_name}
{user_price_section}

Delivery Address:
{street}, {area}, {landmark}, {full_address}

Thank you for shopping with us!
— Team SmartStore
"""

        # 🚀 Send mails
        admin_email = EmailMessage(
            subject="🛒 New Order Received",
            body=force_str(admin_message),
            from_email="companypvtltd35@gmail.com",
            to=["hasansuhail392@gmail.com"],
        )
        admin_email.send(fail_silently=False)

        if email:
            user_email = EmailMessage(
                subject=f"Order Confirmation — {product_name}",
                body=force_str(user_message),
                from_email="companypvtltd35@gmail.com",
                to=[email],
            )
            user_email.send(fail_silently=False)

        # ✅ Clear session after order (avoid data mix)
        for key in ['product_name', 'product_price', 'product_offer', 'product_final_price']:
            if key in request.session:
                del request.session[key]

        return redirect("payment_success")

    return render(request, "buy_now.html")


#----------------------------------------orderviews page for payment access------------------------------------------
