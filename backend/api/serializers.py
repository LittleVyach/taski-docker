"""Missing docstring in public package."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Missing docstring in public package."""

    class Meta:
        """Missing docstring in public package."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
