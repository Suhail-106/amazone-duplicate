from django.db import models

class vocalforlocal(models.Model):
    image = models.URLField(max_length=200)
    logo = models.URLField(max_length=200, default="please upload logo")
    interestincontent = models.CharField(max_length=100, default="Get Festive ready")
    price = models.DecimalField(max_digits=5,decimal_places=0,default="499")
    offer = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.interestincontent
    
class vocalforlocal1(models.Model):
    image1 = models.URLField(max_length=200)
    logo1 = models.URLField(max_length=200, default="please upload logo")
    interestincontent1 = models.CharField(max_length=100, default="Get Festive ready")
    price1 = models.DecimalField(max_digits=5,decimal_places=0,default="499")
    offer1 = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.interestincontent1

class vocalforlocal2(models.Model):
    image2 = models.URLField(max_length=200)
    logo2 = models.URLField(max_length=200, default="please upload logo")
    interestincontent2 = models.CharField(max_length=100, default="Get Festive ready")
    price2 = models.DecimalField(max_digits=5,decimal_places=0,default="499")
    offer2 = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.interestincontent2       
    

class shopclothing(models.Model):
    imageshopclothing = models.URLField(max_length=200)
    contentshopclothing = models.CharField(max_length=100,default="tops & t-shirts")
    priceshopclothing = models.DecimalField(max_digits=5,decimal_places=0)  

    def __str__(self):
        return self.contentshopclothing  
    
class shopfootwear(models.Model):
    imageshopfootwear = models.URLField(max_length=200)
    contentshopfootwear = models.CharField(max_length=100,default="tops & t-shirts")
    priceshopfootwear = models.DecimalField(max_digits=5,decimal_places=0)  

    def __str__(self):
        return self.contentshopfootwear     
    
class Budget_Add_Ons(models.Model):
    imageshopBudget = models.URLField(max_length=200)
    contentshopBudget = models.CharField(max_length=100,default="tops & t-shirts")
    priceshopBudget = models.DecimalField(max_digits=5,decimal_places=0)  

    def __str__(self):
        return self.contentshopBudget        


class shopBeauty(models.Model):
    imageshopBeauty = models.URLField(max_length=200)
    contentshopBeauty = models.CharField(max_length=100,default="skincare")
    priceshopBeauty = models.DecimalField(max_digits=5,decimal_places=0)  

    def __str__(self):
        return self.contentshopBeauty       
# Create your models here.
