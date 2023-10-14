from django.shortcuts import render, redirect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from base.forms import CustomUserCreationForm, LoginForm


# Create your views here.
def home(request):
    return render(request, "index.html")


@sensitive_post_parameters("username", "password")
def sign_up(request):
    # User shouldn't be allowed to sign-up if already logged in
    if request.user.is_authenticated:
        return redirect("home")

    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occurred while submitting the form!")

    return render(request, "signup.html", {"form": form})


@sensitive_post_parameters("username", "password")
def login_page(request):
    # User shouldn't be allowed to re-login if already logged in
    if request.user.is_authenticated:
        return redirect("home")

    username_err = ""
    validation_err = ""
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data.get("username").lower())
            except:
                username_err = "A user with that username does not exist."

            user = authenticate(request, username=form.cleaned_data.get("username").lower(), password=form.cleaned_data.get("password"))

            if user is not None:
                login(request, user)
                return redirect("home")
            elif username_err == "":
                validation_err = "Username or password is invalid."

    return render(request, "login.html", {"form": form, "username_error": username_err, "validation_error": validation_err})


def logout_user(request):
    logout(request)
    return redirect("home")
