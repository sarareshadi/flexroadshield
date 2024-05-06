from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost 

def BlogList(request):
    posts = BlogPost.objects.all()   
    return render(
    request, 
    'blog/bloglist.html', 
    {'posts': posts},
    )

def BlogDetails(request,slug):
    post = get_object_or_404(BlogPost, slug=slug, status = BlogPost.Status.PUBLISHED)
    return render (
        request,
        'blog/blogdetails.html',
        {'post': post},
    )