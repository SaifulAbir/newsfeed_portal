from celery import shared_task
from news.utils import fetch_top_headlines
from settings.models import Country


@shared_task
def fetch_news():
    country_list = Country.objects.all()
    for country in country_list:
        fetch_top_headlines(country.name)