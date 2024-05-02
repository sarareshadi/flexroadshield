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
        page_title='About us'
    )
    return render(
        request,
        'about.html',
        context

    )
