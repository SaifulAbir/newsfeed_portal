from django.db import models
# Create your models here.
from django.db.models.signals import pre_save
from newsfeed_portal.models import newsfeedPortalModel, populate_time_info
from resources import strings_settings


class Country(newsfeedPortalModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_settings.COUNTRY_VERBOSE_NAME
        verbose_name_plural = strings_settings.COUNTRY_VERBOSE_NAME_PLURAL
        db_table = 'countries'

    def __str__(self):
        return self.name


class Source(newsfeedPortalModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_settings.SOURCE_VERBOSE_NAME
        verbose_name_plural = strings_settings.SOURCE_VERBOSE_NAME_PLURAL
        db_table = 'sources'

    def __str__(self):
        return self.name


class Keyword(newsfeedPortalModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = strings_settings.KEYWORD_VERBOSE_NAME
        verbose_name_plural = strings_settings.KEYWORD_VERBOSE_NAME_PLURAL
        db_table = 'keywords'

    def __str__(self):
        return self.name


class Settings(newsfeedPortalModel):
    countries = models.ManyToManyField('Country', blank=True, related_name='skill_set')
    sources = models.ManyToManyField('Source', blank=True, related_name='skill_set')
    keywords = models.ManyToManyField('Keyword', blank=True, related_name='skill_set')

    class Meta:
        verbose_name = strings_settings.SETTINGS_VERBOSE_NAME
        verbose_name_plural = strings_settings.SETTINGS_VERBOSE_NAME_PLURAL
        db_table = 'settings'


pre_save.connect(populate_time_info, sender=Settings)
pre_save.connect(populate_time_info, sender=Keyword)
pre_save.connect(populate_time_info, sender=Source)
pre_save.connect(populate_time_info, sender=Country)
