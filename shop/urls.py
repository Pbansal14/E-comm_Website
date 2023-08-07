from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="Shop"),
    path("register/", views.register, name="Register"),
    path("login/", views.loginn, name="Login"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("trending/", views.trending, name="Trending"),
    path("logout/",views.logoutt, name="LogOut"),
    path("recommend/",views.recommend, name="Recommend"),
]