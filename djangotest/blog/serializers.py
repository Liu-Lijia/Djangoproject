# serializers.py
from rest_framework import serializers
from .models import BlogArticles

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticles
        fields = '__all__'