from django.db import models
import datetime


class Article(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    cover_image = models.TextField(blank=True)
    article_body = models.TextField(blank=True)
    published_at = models.DateTimeField(
        default=datetime.date.today, blank=True, null=True)

    def __str__(self):
        return self.title
