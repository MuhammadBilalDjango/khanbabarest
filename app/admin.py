from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)
# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','email','mobile','city','address']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted','actualprice','discription','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderStatusModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','order_time','status']
