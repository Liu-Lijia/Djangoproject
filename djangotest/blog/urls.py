
from . import views
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import NotesViewSet

router = routers.DefaultRouter()
router.register(r'blog', NotesViewSet)

urlpatterns = [
    # url(r'^$', views.blog_title, name="blog_title"),
    path('', include(router.urls)),
]
