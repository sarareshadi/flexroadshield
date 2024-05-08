from django.shortcuts import render


def HomeView(request):
    context = dict(
        page_title='Home'
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


def ContactView(request):
    context = dict(
        page_title='Contact Us'
    )
    return render(
        request,
        'contact.html',
        context
    )


def ProjectsView(request):
    context = dict(
        page_title='Projects'
    )
    return render(
        request,
        'Projects.html',
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
