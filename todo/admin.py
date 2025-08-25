from .models import Task
from django.contrib import admin

# Register your models here.
class Taskadmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)

admin.site.register(Task, Taskadmin)
