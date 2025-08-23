from django.shortcuts import render
from  django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .forms import MessageForm
from portfolio.forms import MessageForm
from .models import FAQ, Hero, SkillsSection, Work, WorkSection, About, Skill
# Create your views here.
def home(request):
    hero = Hero.objects.first()
    work_section = WorkSection.objects.first()
    works = Work.objects.all()[:3]
    about = About.objects.first() 
    skills = Skill.objects.all()[:3]
    skillsdes = SkillsSection.objects.first()
    faq = FAQ.objects.all()

    context = {
        "hero": hero,
        "work_section": work_section,
        "works": works,
        "about": about,
        "skills": skills,
        "skillsdes": skillsdes,
        "faq" : faq,
        "form": MessageForm(),  # Add the form to the context
    }
    return render(request, "portfolio/home.html", context)



def works_view(request):
    section = WorkSection.objects.first()   # Get the heading/subheading
    works = Work.objects.all()
    return render(request, "works.html", {"section": section, "works": works})


def skill(request):
    skills = Skill.objects.all()
    skillsdes = SkillsSection.objects.first()
    return render(request, "portfolio/skill.html", {"skills": skills, "skillsdes": skillsdes})


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            # Send email 
            send_mail(  
                subject='Alert ! you got message from your portfolio',
                message = f"From:{message.email}\n\n{message.message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["anushkapandey427@gmail.com"],
            )
            return HttpResponse("Message sent successfully!")
    else:
        form = MessageForm()
    return render(request, 'portfolio/contact.html')

def blog(request):
    return render(request, 'portfolio/blog.html')

def about_view(request):
    about = About.objects.first()  # fetch the first record
    return render(request, "portfolio/about.html", {"about": about})
