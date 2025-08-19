from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog, name='blog'),
    path('skill/', views.skill, name='skill'),
    path('work/', views.works_view, name='work'),

]
if settings.DEBUG:  # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)