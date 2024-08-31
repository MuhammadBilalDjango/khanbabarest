from django.shortcuts import render,redirect
from .models import Customer,Product,Cart,OrderPlaced
from django.views import View
from django.contrib import messages
from .forms import CustomerRegisterForm,CustomerProfileForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect,JsonResponse
from django.db.models import Q

from django.contrib import messages

# Create your views here.

#def base(request):
#    return render(request,'home.html')

class HomeView(View):
    def get(self,request):
        product = Product.objects.filter()
        special = Product.objects.filter(category='SP')
        return render(request,'home.html',{'product':product,'special':special})



class OurMenuView(View):
    def get(self,request):
        pizza = Product.objects.filter(category='P')
        burger = Product.objects.filter(category='B')
        fries = Product.objects.filter(category='FR')
        cake = Product.objects.filter(category='CC')
        icecream = Product.objects.filter(category='IC')
        return render(request,'ourmenu.html',{'pizza':pizza,'burger':burger,'fries':fries,'cake':cake,'icecream':icecream})





#def ourmenu(request):
#    return render(request,'ourmenu.html')


class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'productdetail.html',{'product':product})


class SpecialProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        specail = Product.objects.filter(category='SP')
        return render(request,'specialproductdetail.html',{'product':product,'specail':specail})



#def productdetail(request):
#    return render(request,'productdetail.html')

class SpecialDealsView(View):
    def get(self,request):
        special = Product.objects.filter(category='SP')
        return render(request,'specialdeals.html' , {'special':special})


#def specialdeals(request):
#    return render(request,'specialdeals.html')


def addcart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')


def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        quantity = 0
        amount = 0
        shipping = 200
        total = 0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted)
                amount += tempamount
                total = amount+shipping
                quantity +=1
            return render(request,'cart.html',{'carts':cart,'quant':quantity,'amount':amount,'total':total})
        else:
            return render(request,'emptycart.html')





def pluscart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0
        total = 0
        shipping = 200
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted)
            amount +=tempamount
            total = amount

        data = {
                'quantity':c.quantity,
                'amount':amount,
                'total':total+shipping,
            }
        return JsonResponse(data)


def minuscart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0
        total = 0
        shipping = 200
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted)
            amount +=tempamount
            total = amount

        data = {
                'quantity':c.quantity,
                'amount':amount,
                'total':total + shipping
            }
        return JsonResponse(data)


def removecart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 200
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount+=tempamount
            total_amount = amount
        data={

            'amount':amount,
            'total_amount':total_amount + shipping_amount
        }
        return JsonResponse(data)



def aboutus(request):
    return render(request,'aboutus.html')


#def profile(request):
#    return render(request,'profile.html')

class ProfileView(View):
    def get(self,reqeust):
        form = CustomerProfileForm()
        return render(reqeust,'profile.html',{'form':form})

    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            reg = Customer(user=usr,name=name,mobile=mobile,city=city,address=address)
            reg.save()
            messages.success(request,'Profile Updated SuccessFully')
            profile = Customer.objects.all()          
        return render(request,'profile.html',{'form':form,'profile':profile})


#def login(request):
#    return render(request,'login.html')

#def signup(request):
#    return render(request,'signup.html')

class CustomerRegisterView(View):
    def get(self,reqeust):
        form = CustomerRegisterForm()
        return render(reqeust,'signup.html',{'form':form})
    def post(self,request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registered Successfully')
            form.save()
        return render(request,'signup.html',{'form':form})


def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0
    shipping = 200
    total = 0
    quantity = 0
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]
    if cart_items:
        for p in cart_product:
            temp = (p.quantity * p.product.discounted)
            amount +=temp
            quantity+=1
        total = amount+shipping 
    return render(request,'checkout.html',{'add':add,'total':total,'cart_items':cart_items})


def payment_done(request):
    user= request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders')




def orderreceived(request):
    op = OrderPlaced.objects.filter(user=request.user)
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]
    amount = 0
    shipping = 200
    total = 0
    if cart_product:
        for p in cart_product:
            temp = (p.quantity * p.product.discounted)
            amount +=temp
            total = amount+shipping
    return render(request,'orders.html',{'order_placed':op,'total':total})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('accounts/login')