# urls.py
from django.urls import include, path
from rest_framework import routers
from .views import NotesViewSet

router = routers.DefaultRouter()
router.register(r'notes', NotesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]