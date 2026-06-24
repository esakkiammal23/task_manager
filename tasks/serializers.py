from rest_framework import serializers
from .models import Task

class Task2(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'
