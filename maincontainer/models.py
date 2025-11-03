from django.db import models
from django.utils.text import slugify
from datetime import date
from django.contrib.auth.models import User



class main(models.Model):
    bgimage = models.URLField(max_length=200)
    heading = models.CharField(max_length=200)
    heading2 = models.CharField(max_length=200)
    paragraph = models.CharField(max_length=200, default="Top brands")
    paragraph2 = models.CharField(max_length=200, default="Latest brands")
    Term = models.CharField(max_length=200, default="Term and condition")
    bgimage2 = models.URLField(max_length=200, default="please fill the bg removal image")

    def __str__(self):
        return self.heading2
    
class product(models.Model):
    header = models.CharField(max_length=200)
    image1 = models.URLField(max_length=200)
    content1 = models.CharField(max_length=100, default="Air conditioner")
    price1 = models.DecimalField(max_digits=10, decimal_places=2, default="100")
    off171 = models.DecimalField(max_digits=10, decimal_places=2, default="10")

    image2 = models.URLField(max_length=200)
    content2 = models.CharField(max_length=100, default="refgeritor")
    price2 = models.DecimalField(max_digits=10, decimal_places=2, default="100")
    off172 = models.DecimalField(max_digits=10, decimal_places=2, default="10")

    image3 = models.URLField(max_length=200)
    content3 = models.CharField(max_length=100, default="Microwaves")
    price3 = models.DecimalField(max_digits=10, decimal_places=2, default="100")
    off173 = models.DecimalField(max_digits=10, decimal_places=2, default="10")
    
    image4 = models.URLField(max_length=200)
    content4 = models.CharField(max_length=100, default="washing machines")
    price4 = models.DecimalField(max_digits=10, decimal_places=2, default="100")
    off174 = models.DecimalField(max_digits=10, decimal_places=2, default="10")

    def __str__(self):
        return self.content1
   
             
class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=100, default="store etc")  # like "Microwave"
    price = models.DecimalField(max_digits=10, decimal_places=2, default="250")
    quantity = models.IntegerField(default=1)
    off174 = models.DecimalField(max_digits=10, decimal_places=2, default="0")

    def __str__(self):
        return f"{self.content} x{self.quantity}"
    
    def offer(self):
        discount = self.price * self.off174 / 100 
        return round(self.price - discount , 2)* self.quantity
    
    

    

class actiontoys(models.Model):
    header1 = models.CharField(max_length=200, default=None, blank=True, null=True)
    actionimage = models.URLField(max_length=200)   

    def __str__(self):
        return str(self.header1) if self.header1 else "No header" 
    
class mobile(models.Model):
    header2 = models.CharField(max_length=200, default=None, blank=True, null=True)
    imagemobile = models.URLField(max_length=200)
    offermobile = models.DecimalField(max_digits=10, decimal_places=2, default="44")
    mrpmobile = models.DecimalField(max_digits=10, decimal_places=2, default="80")
    nameofmobile = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.nameofmobile
    

class Fresh(models.Model):
    bgimagefresh = models.URLField(max_length=200)
    vegitablebimagefresh = models.URLField(max_length=200)
    nameoffresh = models.CharField(max_length=100, default="name of vegitables")
    headingfresh1 = models.CharField(max_length=150, default="fresh quality")
    paragraphfresh = models.CharField(max_length=100, default="Eat Green, Life Green")
    paragraphfresh1 = models.CharField(max_length=100, default="100% fresh product available")
    pricefresh = models.DecimalField(max_digits=10, decimal_places=1)
    offerfresh = models.DecimalField(max_digits=5, decimal_places=1)
    Termfresh = models.CharField(max_length=200, default="Term and condition")
    
    def __str__(self):
        return self.nameoffresh

class mainmobile(models.Model):
    bgmainimagembile = models.URLField(max_length=200,default="black background image of marvels")
    mainimagemobile = models.URLField(max_length=200)
    nameofmmobile = models.CharField(max_length=200,default="mobile with models")
    specsofmmobileRamrom = models.CharField(max_length=200,default="Titanium, 6GB RAM, 128GB Storage")
    specsofcamera = models.CharField(max_length=100,default="50MP + 2MP - 16MP Front Camera ")
    specsofbattery = models.CharField(max_length=200,default="6500 mAh Large Capacity Battery")
    specsfofprocessor = models.CharField(max_length=200,default="Dimensity 7300 Processor")
    specsofdurability = models.CharField(max_length=200,default="Military-Grade Durability")
    mainmratings = models.DecimalField(max_digits=4, decimal_places=0)
    mainmdeals = models.CharField(max_length=100,default="freedom sale deals")
    mainmprice = models.DecimalField(max_digits=6,decimal_places=0)
    mainmmrp = models.DecimalField(max_digits=6,decimal_places=0)
    mainmoffer = models.DecimalField(max_digits=2, decimal_places=0)
    mainmofferoncreditcard = models.DecimalField(max_digits=2,decimal_places=0)
    mainmtodaydate = models.DateField(default=date.today)
   
    def __str__(self):
     return self.nameofmmobile
    

class electronicslaptop(models.Model):
    laptopname = models.CharField(max_length=100,default="name of laptop")
    laptopimage = models.URLField(max_length=200)
    laptopoffer = models.DecimalField(max_digits=2, decimal_places=0)
    laptopmrpprice = models.DecimalField(max_digits=5, decimal_places=0)    

    def __str__(self):
        return self.laptopname
    
class electronicsheadphones(models.Model):
    headphonesname = models.CharField(max_length=100,default="name of laptop")
    headphonesimage = models.URLField(max_length=200)
    headphonesoffer = models.DecimalField(max_digits=2, decimal_places=0)
    headphonesmrpprice = models.DecimalField(max_digits=5, decimal_places=0)    

    def __str__(self):
        return self.headphonesname   

class electronicsstored(models.Model):
    storedname = models.CharField(max_length=100,default="name of laptop")
    storedimage = models.URLField(max_length=200)
    storedoffer = models.DecimalField(max_digits=2, decimal_places=0)
    storedmrpprice = models.DecimalField(max_digits=5, decimal_places=0)    

    def __str__(self):
        return self.storedname        
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)   

    def __str__(self):
        return self.user.username 

class datasave(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_otp = models.CharField(max_length=6, blank=True, default='000000')
    confirmpassword = models.CharField(max_length=50)
    session_otp = models.CharField(max_length=6, blank=True, default='000000')
   

    def __str__(self):
        return self.username
    





from django.db import models

class UserAddress(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200, blank=True, null=True)
    full_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(default="12")


    def __str__(self):
        return f"{self.name} - {self.area}"


#for mobile view ----------------------------------------------------------------------
