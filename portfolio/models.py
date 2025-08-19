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

    


