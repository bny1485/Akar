from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from Post.models import Post as MyPost


def home(request):
    """ This function is responsible for home page """
    my_post = MyPost.objects.all()
    context = {
        "qs": my_post
    }
    print(context)
    return render(request, 'home.html', context)


# TODO if user is login can not come to this function
# TODO get email varification
USER = get_user_model()
def register_def(request):
    if request.user.is_authenticated:
        return redirect('/')
    Form = RegisterForm(request.POST or None)
    context = {"form": Form}
    if Form.is_valid():
        USR_NAME = Form.cleaned_data.get("usr_name")
        EMAIL = Form.cleaned_data.get("email")
        PASSWD = Form.cleaned_data.get("passwd")
        user = USER.objects.create_user(
            username=USR_NAME, email=EMAIL, password=PASSWD)
        login(request, user)
        context["form"] = RegisterForm()
        return redirect("/")

    return render(request, 'register.html', context)


# TODO better respose for no uesr
# TODO if user is login go to home page
# TODO if user is login can not come to this function
# TODO brute force attack
# TODO get email varification
def login_def(request):
    if request.user.is_authenticated:
        return redirect("/")
    Form = LoginForm(request.POST or None)
    context = {"form": Form}
    if Form.is_valid():
        print(Form.cleaned_data)
        USR_NAME = Form.cleaned_data.get("usr_name")
        PASSWD = Form.cleaned_data.get("passwd")
        user = authenticate(request, username=USR_NAME, password=PASSWD)
        if user is not None:
            login(request, user)
            context["form"] = LoginForm()
            return redirect("/")
        else:
            print("user is None.\nI am in else")

    return render(request, 'login.html', context)


def about_me(request):
    """ This function is responsible for about me page """
    programmer = {
        "name": "Benyamin",
        "last_name": "Mahmoudyam",
        "Email": "benyaminmahmoudyan@gmail.com",
    }
    return render(request, 'about-me.html', programmer)


# TODO Efficient design
def CV(request):
    """ This function is responsible for CV """
    return render(request, 'CV.html')


def Album(request):
    """ This function show all my post """
    my_post = MyPost.objects.all()
    context = {"qs": my_post}
    return render(request, 'Album.html')
