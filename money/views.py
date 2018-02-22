from django.shortcuts import render, redirect
from .models import Business
from .forms import BusinessForm, SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate



def list(request):
	object_list = Business.objects.all()
	context = {
	"cash": object_list
	}
	return render(request, 'list.html', context)

def detail(request, business_id):
	object_list = Business.objects.get(id=business_id)
	context = {
	"object_list": object_list
	}
	return render(request, 'detail.html', context)

def create(request):
	form = BusinessForm(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('list')
	context = {
	"form": form,
	}
	return render(request, 'create.html', context)

def update(request, business_id):
	instance = Business.objects.get(id=business_id)
	form = BusinessForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect('list')
	context = {
	"form": form,
	"instance": instance,
	}
	return render(request, 'update.html', context)

def delete(request, business_id):
	object_list = Business.objects.get(id=business_id).delete()
	return redirect('list')

def signup(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			login(request, user)
			return redirect("list")
	context = {
	"form": form 
	}
	return render(request, 'signup.html', context)


def userlogout(request):
    logout(request)
    return redirect('login')


def userlogin(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("list")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)
