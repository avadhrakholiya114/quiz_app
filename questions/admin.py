from django.contrib import admin
from .models import Question,Answer
# Register your models here.

class AnsewerInline(admin.TabularInline):
    model = Answer

class Questionadmin(admin.ModelAdmin):
    inlines = [AnsewerInline]

admin.site.register(Question,Questionadmin)
admin.site.register(Answer)