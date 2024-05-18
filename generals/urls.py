from django.urls import path

from . import views

app_name = 'generals'


urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('projects/', views.ProjectsView, name='projects'),
    path('services/', views.ServicesView, name='services'),
]
