from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
path('bloglist/', views.BlogList, name='bloglist'),
path('blogdetails/', views.BlogDetails, name='blogdetails'),
path('', views.BlogList, name= 'blog'),
]