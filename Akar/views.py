from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm


def register_function(request):
    if request.method == "POST":
        Form = RegisterForm(request.POST)
    else:
        Form = RegisterForm()
    return render(request, 'register.html', {'form': Form})


def login(request):
    if request.method == "POST":
        print(request.POST.get("usr_name"))
        print(request.POST.get("passwd"))

    return render(request, 'login.html', {})


def home_page(request):
    return render(request, 'home_page.html', {})


def about_me_page(request):
    programmer = {
        "name": "Benyamin",
        "last_name": "Mahmoudyam",
        "Email": "benyaminmahmoudyan@gmail.com",
    }
    return render(request, 'about-me.html', {})
