from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import BlogArticles
from .serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = BlogArticles.objects.all()
    serializer_class = NoteSerializer

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs":blogs})