from django.urls import path
from news.api import NewsFeedAPI

urlpatterns = [
    path('news-feed/', NewsFeedAPI.as_view()),
]