from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save, post_save
from newsfeed_portal.models import newsfeedPortalModel, populate_time_info
from resources import strings_news
from settings.models import Settings


class News(newsfeedPortalModel):
    headline = models.CharField(max_length=255, unique=True)
    thumbnail = models.CharField(max_length=500)
    source_of_news = models.CharField(max_length=100, null=True)
    country_of_news = models.CharField(max_length=100)
    news_url = models.CharField(max_length=500)

    class Meta:
        verbose_name = strings_news.NEWS_VERBOSE_NAME
        verbose_name_plural = strings_news.NEWS_VERBOSE_NAME_PLURAL
        db_table = 'news'

    def __str__(self):
        return self.headline


def after_news_save(sender, instance:News, *args, **kwargs):
    settings_list = Settings.objects.all()
    for each_user in settings_list:
        country_list = each_user.countries.values_list('name', flat=True)
        source_list = each_user.sources.values_list('name', flat=True)
        keyword_list = each_user.keywords.values_list('name', flat=True)

        if instance.country_of_news in country_list and instance.source_of_news in source_list:
            for keyword in keyword_list:
                if keyword in instance.headline:
                    send_mail(
                        'You have one new top headline in your newsfeed',
                        'Here is the headline - '+instance.headline,
                        'saiful.abir20@gmail.com',
                        [each_user.user.email],
                        fail_silently=False,
                    )


pre_save.connect(populate_time_info, sender=News)
post_save.connect(after_news_save, sender=News)
