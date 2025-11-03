from django.shortcuts import render
from maincontainer.models import main, product as productMOdel, CartItem, actiontoys, electronicsstored, mobile,electronicslaptop, electronicsheadphones
from mobileviews.models import mainob, cartItemMobile, mainob2, mainob3,  bestseller
from maincontainer.views import filtered_products1


def get_discount(price,off):
    return round(price - (price * off /100), 2)

def allcontent(request):
    allmain = main.objects.all()
    allproduct = productMOdel.objects.all()
    for product in allproduct:
        product.final_price1 = get_discount(product.price1, product.off171)
        product.final_price2 = get_discount(product.price2, product.off172)
        product.final_price3 = get_discount(product.price3, product.off173)
        product.final_price4 = get_discount(product.price4, product.off174)



    allCartItem = CartItem.objects.all()
    allactiontoys = actiontoys.objects.all()
    allmobile = mobile.objects.all()
    allelectronicslaptop = electronicslaptop.objects.all()
    allelectronicsheadphones = electronicsheadphones.objects.all()
    allelectronicsstored = electronicsstored.objects.all()
    for laptop in allelectronicslaptop:
        laptop.final_price = get_discount(laptop.laptopmrpprice, laptop.laptopoffer)

    for stored in allelectronicsstored:
        stored.final_pricestored = get_discount(stored.storedmrpprice, stored.storedoffer)

    for headphones in allelectronicsheadphones:
        headphones.final_priceheadphones = get_discount(headphones.headphonesmrpprice, headphones.headphonesoffer)
    

    for mob in allmobile:
        mob.final_price = get_discount(mob.mrpmobile, mob.offermobile)
    
    #mobileveiws.models

    allmainob = mainob.objects.all()
    allcartItemMobile = cartItemMobile.objects.all()
    allmainob2 = mainob2.objects.all()
    allmainob3 = mainob3.objects.all()
    allbestseller = bestseller.objects.all()

    return render(request,
    'allcontent.html',{'main':allmain,
    'bestseller':allbestseller,
    'actionToys':allactiontoys,
    'products':allproduct,
    'mobile':allmobile,
    'electronicslaptop':allelectronicslaptop,
    'electronicsheadphones':allelectronicsheadphones,
    'electronicsstored':allelectronicsstored,})
    

# Create your views here.
