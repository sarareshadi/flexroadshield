from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost 
from django.core.paginator import Paginator

def BlogList(request):
    posts_list = BlogPost.objects.filter(status='PB')   
    paginator = Paginator(posts_list, 9)  
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
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