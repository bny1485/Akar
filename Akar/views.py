from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm


USER = get_user_model()
def register_def(request):
    Form = RegisterForm(request.POST or None)
    if Form.is_valid():
        print(Form.cleaned_data)
        USR_NAME = Form.cleaned_data.get("usr_name")
        EMAIL = Form.cleaned_data.get("email")
        PASSWD = Form.cleaned_data.get("passwd")
        USER.objects.create_user(username=USR_NAME, email=EMAIL, password=PASSWD)

    return render(request, 'register.html', {'form': Form})


def login_def(request):
    Form = LoginForm(request.POST or None)
    context = {"form": Form}
    if Form.is_valid():
        USR_NAME = Form.cleaned_data.get("usr_name")
        PASSWD = Form.cleaned_data.get("passwd")
        user = authenticate(request, username=USR_NAME, password=PASSWD)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/about-me")
        else:
            print("user is None.\nI am in else")

    return render(request, 'login.html', context)


def home_page(request):
    return render(request, 'home_page.html', {})


def about_me_page(request):
    programmer = {
        "name": "Benyamin",
        "last_name": "Mahmoudyam",
        "Email": "benyaminmahmoudyan@gmail.com",
    }
    return render(request, 'about-me.html', {})
