from django.shortcuts import render
from .models import Hero, Work, WorkSection
# Create your views here.
def home(request):
    hero = Hero.objects.first()
    works = Work.objects.all()
    return render(request, 'portfolio/home.html', {
        'hero': hero,
        'works': works      
    })

def works_view(request):
    section = WorkSection.objects.first()   # Get the heading/subheading
    works = Work.objects.all()
    return render(request, "works.html", {"section": section, "works": works})
def skill(request): 
    return render(request, 'portfolio/skill.html')
def contact(request):
    return render(request, 'portfolio/contact.html')
def blog(request):
    return render(request, 'portfolio/blog.html')
def about(request):
    return render(request, 'portfolio/about.html')  
