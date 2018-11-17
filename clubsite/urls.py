from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='clubsite-home'),
    path('news/', views.news, name='clubsite-news'),

]
