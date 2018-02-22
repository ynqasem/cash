from .models import Business

from django import forms

from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
	class Meta:
		model = Business
		fields = '__all__'

		widgets = {
		"established": forms.DateInput(attrs={"type":"date"})
		}

class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "email", "firstname", "lastname", "password"]
		widgets ={
		"password": forms.PasswordInput()
		}

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())