from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=200)  
def __str__(self):
    return str(self.id)



ORDER_CHOICE = {
    ('P' , 'Pizza'),
    ('B','Burger'),
    ('CC','CupCake'),
    ('FR','Fries'),
    ('IC','Icecream'),
    ('SP','Special'),
}


class Product(models.Model):
    title = models.CharField(max_length=100)
    discounted = models.IntegerField()
    actualprice = models.IntegerField()
    discription = models.TextField(max_length=200)
    category = models.CharField(choices=ORDER_CHOICE,max_length=2)
    product_image = models.ImageField(upload_to='productimg')
def __str__(self):
    return str(self.id)



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)






ORDER_STATUS = {
    ('A','Accepted'),
    ('R','Getting Ready'),
    ('P','Packed'),
    ('D','Dispached'),
    ('DI','Delivered'),
    ('C','Canceled')

}

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    order_time = models.TimeField(auto_now=True)
    status = models.CharField(choices=ORDER_STATUS,max_length=3,default='Pending')
    @property
    def total_cost(self):
        temp = self.quantity * self.product.discounted
        total = temp+200
        return  total