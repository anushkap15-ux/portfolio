from django.contrib import admin
from .models import FAQ, Hero, SkillsSection , Work , WorkSection ,About, Skill


admin.site.register(Hero)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("heading", "demo_link", "source_code_link", "created_at")
    search_fields = ("heading", "description")

    
@admin.register(WorkSection)
class WorkSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "subheading")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage",)
    

@admin.register(SkillsSection)
class SkillsSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)


