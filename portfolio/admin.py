from django.contrib import admin
from .models import Hero , Work , WorkSection


admin.site.register(Hero)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("heading", "demo_link", "source_code_link", "created_at")
    search_fields = ("heading", "description")
@admin.register(WorkSection)
class WorkSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "subheading")

