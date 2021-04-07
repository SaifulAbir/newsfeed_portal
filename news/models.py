from django.db import models
from newsfeed_portal.models import newsfeedPortalModel


class News(newsfeedPortalModel):
    headline = models.CharField(max_length=255, unique=True)
    thumbnail = models.SlugField(max_length=255)
    source_of_news = models.CharField(max_length=50)
    country_of_news = models.CharField(max_length=255)
