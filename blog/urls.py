from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
path('', views.BlogList, name= 'blog_home'),   
# path('bloglist/', views.BlogList, name='bloglist'),
path('blogdetails/<int:id>/', views.BlogDetails, name='blogdetails'),

]