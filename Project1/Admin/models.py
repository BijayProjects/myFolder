from django.db import models
import datetime

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=50)
    paragraph = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class Services(models.Model):
    delivery = models.CharField(max_length=200)
    free_shipping = models.CharField(max_length=200)
    best_quality = models.CharField(max_length=200)
    customer_support = models.CharField(max_length=200)

    def __str__(self):
        return self.delivery
    
class About(models.Model):
    About_me=models.TextField()

class Product(models.Model):
    
    product_name = models.CharField(max_length=100)
    price =  models.IntegerField()
    description = models.TextField()
    image_product = models.ImageField(upload_to="Media")
    VAT = models.CharField( max_length=200, blank=True)

    def __str__(self):
        return self.product_name
    
class Feedbacks(models.Model):
    userName = models.CharField(max_length=200)
    phoneNo = models.CharField(max_length=20)
    email = models.EmailField()
    messages = models.TextField()

    def __str__(self) :
        return self.userName

class Order_Detail(models.Model):
    recipient = models.CharField(max_length=100)
    customer_email = models.EmailField()
    phone_number = models.CharField(max_length=1000)
    address = models.CharField(max_length=200)
    order_creation_date = models.DateTimeField()
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='Order_product_Images')





