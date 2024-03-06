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
