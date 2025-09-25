from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_view, name='about'),
    path('skill/', views.skill, name='skill'),
    path('work/', views.works_view, name='work'),

]
