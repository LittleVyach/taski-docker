"""Missing docstring in public package."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Missing docstring in public package."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
