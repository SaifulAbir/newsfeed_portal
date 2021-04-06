from newsapi import NewsApiClient


def fetch_top_headlines():
    newsapi = NewsApiClient(api_key='7201b6b9554b44c185fc82adcbc5d3e3')
    countrywise_top_headlines = newsapi.get_top_headlines(country='us')
    return countrywise_top_headlines