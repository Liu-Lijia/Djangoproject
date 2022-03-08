
from . import views
from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import NotesViewSet

router = routers.DefaultRouter()
router.register(r'blog', NotesViewSet)

urlpatterns = [
    # 展示blog_title（blog/titles.html）中的HTML
    url(r'^$', views.blog_title, name="blog_title"),

    #以API的方式得到MOdel的数据
    # path('', include(router.urls)),
]
