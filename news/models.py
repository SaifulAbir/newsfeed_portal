from django.db import models
from django.db.models.signals import pre_save
from newsfeed_portal.models import newsfeedPortalModel, populate_time_info
from resources import strings_news


class News(newsfeedPortalModel):
    headline = models.CharField(max_length=255, unique=True)
    thumbnail = models.CharField(max_length=255)
    source_of_news = models.CharField(max_length=50)
    country_of_news = models.CharField(max_length=255)
    news_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = strings_news.NEWS_VERBOSE_NAME
        verbose_name_plural = strings_news.NEWS_VERBOSE_NAME_PLURAL
        db_table = 'news'

    def __str__(self):
        return self.headline


pre_save.connect(populate_time_info, sender=News)
