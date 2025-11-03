from django.db import models
from django.utils.text import slugify

class mainob(models.Model):
    content = models.CharField(max_length=500, default="bazaar")
    image = models.URLField(max_length=200, default="please upload non-background image")
    imagemain = models.URLField(max_length=200,default="upload image")
    crazylower = models.CharField(max_length=200, default="crazylowerprice")
    term = models.CharField(max_length=100, default="T&C apply")
    name = models.CharField(max_length=100, default="Unknown", blank=True, null=True)
    startingprice = models.DecimalField(max_digits=100, decimal_places=0, default="starting 199")

    def __str__(self):
        return self.name

class cartItemMobile(models.Model):
    content = models.CharField(max_length=100, default="store etc")  # like "Microwave"
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    off174 = models.FloatField(default=0)

    def __str__(self):
        return self.content
    

class mainob2(models.Model):
    header = models.CharField(max_length=200, default="please fill this field")
    imagemainob2 = models.URLField(max_length=200)    

    def __str__(self):
        return self.header  
    

class mainob3(models.Model):
    footer = models.CharField(max_length=200, default="fill")
    imagemainob3 = models.URLField(max_length=200)    

    def __str__(self):
        return self.footer
    

class bestseller(models.Model):
    headermatch = models.CharField(max_length=200, default="bestseller")
    Imagem = models.URLField(max_length=200)
    contentm = models.CharField(max_length=300, default="name of watches")
    pricewacth = models.DecimalField(max_digits=10, decimal_places=1)
    
    def __str__(self):
        return self.contentm

# Create your models here.
