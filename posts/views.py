from django.shortcuts import render
import requests
from .models import Article


def get_articles(request):
    all_articles = {}

    API_KEY = 'API_KEY'

    url = 'https://dev.to/api/articles/me/published'

    headers = {'api-key': API_KEY}

    response = requests.get(url, headers=headers)

    data = response.json()

    for i, item in enumerate(data):
        article_data = Article(
            title=data[i]['title'],
            description=data[i]['description'],
            cover_image=data[i]['cover_image'],
            article_body=data[i]['body_markdown'],
            published_at=data[i]['published_at']
        )

        article_data.save()

        all_articles = Article.objects.all().order_by(
            '-published_at').distinct('published_at')

        return render(request, "blog.html", {"all_articles": all_articles})


def blogBody(request, id):
    article = Article.objects.get(id=id)

    return render(request, "blogBody.html", {"article": article})
