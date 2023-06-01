from django.urls import path 
from . import views 

urlpatterns = [
    path('home/',views.MainPage.as_view(),name="home"),
    path("create/",views.CreatePost.as_view())
]
