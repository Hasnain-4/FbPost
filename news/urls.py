from django.urls import path, include
from news import views

urlpatterns = [
    path('news',views.topnews,name='topnews'),
]