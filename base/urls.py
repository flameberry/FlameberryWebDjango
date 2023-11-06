from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

from django_distill import distill_path

urlpatterns = [
    distill_path("", views.home, name="home"),
    distill_path("overview/", views.overview, name="overview"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.sign_up, name="signup"),
]
