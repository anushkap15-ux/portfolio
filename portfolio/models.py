from turtle import title
from django.db import models

# Create your models here.
class Hero(models.Model):
    logo = models.ImageField(upload_to='skill_logos/', blank=True, null=True)
    heading = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    cover_img = models.ImageField(upload_to='cover_photo/',blank=True)
    work_btn = models.CharField(max_length=20)
    def __str__(self):
        return self.heading

from django.db import models

class Work(models.Model):
    heading = models.CharField(max_length=100)                     # Project title
    description = models.TextField(blank=True)                     # Project description
    demo_link = models.URLField(max_length=200, blank=True)        # "See more" button
    source_code_link = models.URLField(max_length=200, blank=True) # GitHub button

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]   # Show latest project first

    def __str__(self):
        return self.heading
    
class WorkSection(models.Model):
    heading = models.CharField(max_length=100, default="Work")   # e.g., "Work"
    subheading = models.TextField(blank=True)                    # e.g., "A curated selection..."

    def __str__(self):
        return self.heading


class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)   # e.g. Full Stack Developer
    intro = models.TextField()                 # short intro paragraph
    description = models.TextField()           # detailed description
    resume_link = models.URLField(blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)
    heading = models.CharField(max_length=100, blank=True, null=True)

    # social links
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    # profile image
    profile_image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    ICON_CHOICES = [
        ("fa-brands fa-html5", "HTML5"),
        ("fa-brands fa-css3-alt", "CSS3"),
        ("fa-brands fa-js", "JavaScript"),
        ("fa-brands fa-java", "Java"),
        ("fa-brands fa-python", "Python"),
        ("fa-solid fa-c", "C"),
        ("fa-brands fa-github", "Git & GitHub"),
        ("fa-solid fa-database", "PLSQL"),
        ("fa-brands fa-react", "React"),
        ("fa-brands fa-node-js", "Node.js"),
        ("fa-brands fa-bootstrap", "Bootstrap"),
        ("fa-brands fa-sass", "Sass"),
        ("fa-brands fa-figma", "Figma"),
        ("fa-brands fa-j", "django"),
    ]

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, choices=ICON_CHOICES, help_text="FontAwesome class")
    percentage = models.PositiveIntegerField(default=0, help_text="Skill level in %")

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

class SkillsSection(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skill_img = models.ImageField(upload_to="skills/", blank=True, null=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
