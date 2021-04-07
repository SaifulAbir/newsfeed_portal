from newsapi import NewsApiClient
from news.models import News


def fetch_top_headlines(country):
    newsapi = NewsApiClient(api_key='7201b6b9554b44c185fc82adcbc5d3e3')
    countrywise_top_headlines = newsapi.get_top_headlines(country=country)
    for each_news in countrywise_top_headlines["articles"]:
        try:
            news_obj = News.objects.get(headline=each_news['title'])
        except News.DoesNotExist:
            news_obj = None
        if not news_obj:
            news_obj = News(headline=each_news['title'], thumbnail=each_news['urlToImage'], source_of_news=each_news['source']['id'],
                            country_of_news=country, news_url=each_news['url'])
            news_obj.save()