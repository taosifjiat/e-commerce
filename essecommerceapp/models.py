from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    price=models.IntegerField()
    image=models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.name
    @property
    def img(self):
        try:
            img_url=self.image.url
        except:
            img_url=''
        return img_url
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True,blank=True,null=True)
    complete=models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total_items(self):
        total=self.orderitem_set.all()
        t=0
        for i in total:
            t=t+i.quantity
        return t
    def get_cart_total_price(self):
        total=self.orderitem_set.all()
        t=0
        for i in total:
            t=t+i.get_total_price
        return t

class Orderitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    oder=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    date=models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return str(self.product.name)
    @property
    def get_total_price(self):
        total=self.product.price * self.quantity
        return total