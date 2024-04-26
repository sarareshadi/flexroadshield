from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import BlogPost

def BlogList(request):
    posts = BlogPost.objects.all()
    
    return render(
    request, 
    'bloglist.html', 
    {'posts': posts},
    )

def BlogDetails(request):    
    return render(
    request, 
    'blogdetails.html',
    )
