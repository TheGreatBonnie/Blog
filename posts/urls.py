from django.urls import path
from .views import get_articles, blogBody


urlpatterns = [
    path("blog", get_articles, name="blog"),
    path("article/<int:id>", blogBody, name="article"),
]
