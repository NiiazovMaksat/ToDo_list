from django.contrib import admin

# Register your models here.
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'status', 'updated_at']
    list_filter = ['status']
    search_fields = ['task', 'updated_at']
    fields = ['task', 'status', 'updated_at', 'description']


admin.site.register(Task, TaskAdmin)