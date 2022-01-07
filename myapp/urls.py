from os import name
from django.urls import path
from . import views


urlpatterns =[
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
    path("page", views.mypage, name="page"),
    path("register", view=views.register_page, name="register"),
    path("dypage/<str:pk>", view=views.dypage, name="dypage")
]