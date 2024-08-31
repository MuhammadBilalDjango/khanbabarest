"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.views import View
from django.contrib.auth import views as auth_view
from app.forms import CustomerLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.base,name="home"),
    path('',views.HomeView.as_view(),name="home"),
    path('ourmenu',views.OurMenuView.as_view(),name="ourmenu"),
    #path('ourmenu',views.ourmenu,name="ourmenu"),
    path('specialdeals/',views.SpecialDealsView.as_view(),name="specialdeals"),
    #path('special',views.specialdeals,name="special"),
    #path('productdetail',views.productdetail,name="productdetail"),
    path('productdetail/<int:pk>',views.ProductDetailView.as_view(),name="productdetail"),
    path('specialproductdetail/<int:pk>',views.SpecialProductDetailView.as_view(),name="specialproductdetail"),
    path('add-to-cart/',views.addcart,name="add-to-cart"),
    path('cart/',views.showcart,name="showcart"),
    path('pluscart/',views.pluscart),
    path('minuscart/',views.minuscart),
    path('removecart/',views.removecart),
    path('about',views.aboutus,name="about"),
    path('logout',views.logout_user,name="logout"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=CustomerLoginForm),name="userlogin"),
    #path('register',views.signup,name="register"),
    path('register',views.CustomerRegisterView.as_view(),name="register"),
    path('checkout/',views.checkout,name="checkout"),
    path('orders/',views.orderreceived,name="orders"),
    path('payment-done',views.payment_done,name="payment-done"),
    #path('check/',views.showcheckout,name="showcheckout"),
    #path('profile',views.profile,name="profile"),
    path('profile',views.ProfileView.as_view(),name="profile"),
    path('orderreceived',views.orderreceived,name="orderreceived")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
