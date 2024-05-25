from django.shortcuts import render

from blog.models import BlogPost

def HomeView(request):
    posts = BlogPost.objects.filter(status=BlogPost.Status.PUBLISHED).order_by('-published_date', '-created_on')[:3]
    context = dict(
        page_title='Home',
        posts=posts
    )
    return render(
        request,
        'home.html',
        context
    )


def AboutView(request):
    context = dict(
        page_title='About Us'
    )
    return render(
        request,
        'about.html',
        context
    )

def ProjectsView(request):
    context = dict(
        page_title='Projects'
    )
    return render(
        request,
        'projects.html',
        context
    )


def ServicesView(request):
    context = dict(
        page_title='Services'
    )
    return render(
        request,
        'services.html',
        context
    )            
