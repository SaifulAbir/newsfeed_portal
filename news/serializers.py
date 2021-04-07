from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('headline', 'thumbnail', 'news_url', 'source_of_news', 'country_of_news')