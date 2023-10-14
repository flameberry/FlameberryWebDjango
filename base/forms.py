from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from base.models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "material-input", "placeholder": "Username", "autocomplete": "off", "autofocus": False}
        )
        self.fields["password1"].widget.attrs.update({"class": "material-input", "placeholder": "New Password"})
        self.fields["password2"].widget.attrs.update({"class": "material-input", "placeholder": "Confirm Password"})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"class": "material-input", "placeholder": "Username", "autocomplete": "off"})

        self.fields["password"].widget.attrs.update({"class": "material-input", "placeholder": "Password"})
