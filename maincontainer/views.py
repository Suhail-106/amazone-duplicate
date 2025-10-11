from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from maincontainer.models import main,Profile,datasave, actiontoys, electronicsstored, electronicsheadphones, CartItem, mobile, electronicslaptop, Fresh, mainmobile, product as ProductModel
from django.db.models import Sum
from mobileviews.models import mainob, cartItemMobile, mainob2, mainob3, mainob4, bestseller
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
    allmainob4 = mainob4.objects.all()

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
        'mainob4':allmainob4,
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

def add_to_cartmobile(request, mobile_id):
    mobile_obj = get_object_or_404(mobile, id=mobile_id)

    matched_nameofmobile = mobile_obj.nameofmobile
    matched_price = mobile_obj.mrpmobile
    matched_offer = mobile_obj.offermobile

    if matched_nameofmobile is None:
        return redirect('home')

    cart_item, created = CartItem.objects.get_or_create(
        product=None,
        content=matched_nameofmobile,
        price=matched_price,
        defaults={'off174': matched_offer, 'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','home'))


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

        total_offer_percentage = (total_offer / total_price_total) * 100 

    return render(request, 'cart.html', {
        'cart_items': cart_items, 'product': allproduct,'total_price': total_price,
        'total_offer': total_offer, 'total_offer_percentage':total_offer_percentage,'mobile': allmobile, 
        'cart_count':total_quantity, 'bestseller':allbestseller, 'fresh': allfresh,'mainmobile':allmainmobile,
        'electronicslaptop':allelectronicslaptop,'electronicsheadphones':allelectronicsheadphones, 'vocalforlocal':allvocalforloacal,
        'vocalforlocal1':allvocalforloacal1,'shopclothing':allshopclothing,
        'shopfootwear':allshopfootwear, 'Budgetaddons':allbudgetaddons, 'shopBeauty':allShopBeauty, 'bedroom':allbedroom,
        
    })


def filtered_products1(request, bestseller_id):
    matched_bestseller = get_object_or_404(bestseller, id=bestseller_id)

    price_watch = matched_bestseller.pricewacth
    name_watch = matched_bestseller.contentm

    if name_watch is None:
        return redirect('filtered_products')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        off174 = 0,
        content = name_watch,
        price = price_watch,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', 'filtered_products'))    


def filtered_products(request):
    matched_data = bestseller.objects.all()
   
    cart_count = CartItem.objects.aggregate(total_qty=Sum('quantity'))['total_qty'] or 0 
    
    return render(request, 'product_list.html', {'matched_data': matched_data,'cart_count':cart_count})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

def fresh(request):
    allfresh = Fresh.objects.all()
    return render(request, 'fresh.html',{'fresh':allfresh})

def fresh_addtocart(request, fresh_id):
    freshcart = get_object_or_404(Fresh, id=fresh_id)

    priceofvegitable = freshcart.pricefresh
    nameofvegitable = freshcart.nameoffresh
    offerofvergitable = freshcart.offerfresh

    if nameofvegitable is None:
        return redirect('fresh')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = nameofvegitable,
        price = priceofvegitable,
        defaults={'quantity':1, 'off174':offerofvergitable}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','fresh'))    

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

    return redirect('mobile')    

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

def storedaddtocart(request, stored_id):
    elstored = get_object_or_404(electronicsstored,id=stored_id)

    nameofelectronicsstored = elstored.storedname
    electronicsstoredoffer = elstored.storedoffer
    electronicsstoredmrpprice = elstored.storedmrpprice

    if nameofelectronicsstored is None:
        return redirect('electronics')
    
    cart_item, created = CartItem.objects.get_or_create(
        product = None,
        content = nameofelectronicsstored,
        price = electronicsstoredmrpprice,
        defaults={'quantity':1,'off174':electronicsstoredoffer}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER','electronics'))        


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



def dashboard(requst):
    pass

def logout(request):
    pass
   
