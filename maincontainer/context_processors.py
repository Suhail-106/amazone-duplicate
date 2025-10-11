from django.shortcuts import render,redirect
from maincontainer.models import CartItem
from mobileviews.models import cartItemMobile
from maincontainer.models import main,Profile,datasave, actiontoys, electronicsstored, electronicsheadphones, CartItem, mobile, electronicslaptop, Fresh, mainmobile, product as ProductModel
from mobileviews.models import mainob, cartItemMobile, mainob2, mainob3, mainob4, bestseller
from Fashion.models import vocalforlocal, vocalforlocal1, vocalforlocal2, shopclothing, shopfootwear,Budget_Add_Ons,shopBeauty
from HomeandKitchen.models import bedroom
from django.db.models import Q
from django.db.models import Sum

def cart_count_processor(request):
    cart_items = CartItem.objects.all()
    cart_itemsmobile = cartItemMobile.objects.all()

    web_cart_quantity = sum(item.quantity for item in cart_items)
    mobile_cart_quantity = sum(item.quantity for item in cart_itemsmobile)

    total_cart_count = web_cart_quantity + mobile_cart_quantity

    return {
        'cart_count': total_cart_count,   # ab dono ka sum hamesha milega
    }

# maincontainer/context_processors.py

def pincode_context(request):
    result = ""
    error = ""
    pincode = request.GET.get("pincode")

    if pincode:
        try:
            pin = int(pincode)
            if len(pincode) != 6:
                error = "Input must be 6 digits"
            elif 110001 <= pin <= 110096:
                result = f"City: New Delhi, Pincode: {pin}"
            elif 400001 <= pin <= 400099:
                result = f"City: Mumbai, Pincode: {pin}"
            elif 560001 <= pin <= 560099:
                result = f"City: Bangalore, Pincode: {pin}"
            elif 208001 <= pin <= 208027:
                result = f"City: Kanpur, Pincode: {pin}"
            elif 226001 <= pin <= 226099:
                result = f"City: Lucknow, Pincode: {pin}"
            elif 380001 <= pin <= 380099:
                result = f"City: Ahmedabad, Pincode: {pin}"
            elif 500001 <= pin <= 501401:
                result = f"City: Hyderabad, Pincode: {pin}"
            elif 700001 <= pin <= 700094:
                result = f"City: Kolkata, Pincode: {pin}"
            else:
                error = "Sorry, I don't know this location"
        except ValueError:
            error = "Please enter only numbers"

    return {
        'result': result,
        'error': error,
    }


def headerall(request):
    #models maincontainer
    allmain = main.objects.all()
    allproduct = ProductModel.objects.all()
    allfresh = Fresh.objects.all()
    allmobile = mobile.objects.all()
    allmainmobile = mainmobile.objects.all()
    allelectronicslaptop = electronicslaptop.objects.all()
    allelectronicsheadphones = electronicsheadphones.objects.all()
    allelectronicsstored = electronicsstored.objects.all()

    #models mobileviews
    allmainob = mainob.objects.all()
    allmainob2 = mainob2.objects.all()
    allmainob3 = mainob3.objects.all()
    allbestseller = bestseller.objects.all()
    
    #models Home&Kitchen
    allbedroom = bedroom.objects.all()

    if request.method == "GET":
        searhingbar = request.GET.get('searchbar')
        if searhingbar != None:
             allmain = main.objects.filter(heading2__icontains = searhingbar)
             allproduct = ProductModel.objects.filter(
               Q(content1__icontains=searhingbar) |
               Q(content2__icontains=searhingbar) |
               Q(content3__icontains=searhingbar) |
               Q(content4__icontains=searhingbar)
          )
             allmobile = mobile.objects.filter(nameofmobile__icontains=searhingbar)
             allfresh = Fresh.objects.filter(nameoffresh__icontains=searhingbar)
             allmainmobile = mainmobile.objects.filter(nameofmmobile__icontains=searhingbar)
             allelectronicslaptop = electronicslaptop.objects.filter(laptopname__icontains=searhingbar)
             allelectronicsheadphones = electronicsheadphones.objects.filter(headphonesname__icontains=searhingbar)
             allelectronicsstored = electronicsstored.objects.filter(storedname__icontains=searhingbar)

             #models mobilviews
             allmainob = mainob.objects.filter(name__icontains=searhingbar)
             allmainob2 = mainob2.objects.filter(header__icontains=searhingbar)
             allmainob3 = mainob3.objects.filter(footer__icontains=searhingbar)
             allbestseller = bestseller.objects.filter(contentm__icontains=searhingbar)

             #models home&kitchen
             allbedroom = bedroom.objects.filter(content__icontains=searhingbar)


    return{
        'main':allmain,
        'product':allproduct,
        'fresh':allfresh,
        'mobile':allmobile,
        'mainmobile':allmainmobile,
        'electronicslaptop':allelectronicslaptop,
        'electronicsheadphones':allelectronicsheadphones,
        'electronicsstored':allelectronicsstored,

        #models mobileviews
        'mainob':allmainob,
        'mainob2':allmainob2,
        'mainob3':allmainob3,
        'bestseller':allbestseller,

        #models home&kitchen
        'bedroom':allbedroom,

    
    }