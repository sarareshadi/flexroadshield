from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def BlogList(request):
    posts_list = BlogPost.objects.filter(status='PB')   

    # posts = paginator.get_page(page_number)

    
    page_number = request.GET.get('page')
    paginator = Paginator(posts_list, 9)  
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
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