from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Customer,Cart
from django.utils.translation import gettext,gettext_lazy as _




class CustomerRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    email = forms.CharField(label="",required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {
            'username':""
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'})
        }



class CustomerLoginForm(AuthenticationForm):
    username = UsernameField(label="",widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'User Name'}))
    password = forms.CharField(label=_(""),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password','placeholder':'Password'}))



class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ['name','mobile','city','address']
        labels = {
            'name':"",
            'mobile':"",
            'city':"",
            'address':"",
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),

        }
