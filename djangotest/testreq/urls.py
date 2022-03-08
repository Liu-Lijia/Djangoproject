# urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ResViewSet

router = routers.DefaultRouter()
router.register(r'testreq', ResViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('phone', views.phone, name='phone'),
    path('id', views.id,name='id'),
    path('name', views.name,name='name'),
    path('get_csrf_token', views.get_csrf_token,name='get_csrf_token'),
]