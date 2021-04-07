from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import News
from news.serializers import NewsSerializer
from settings.models import Settings


class NewsFeedAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NewsSerializer
    def get_queryset(self):
        request = self.request
        settings_obj = Settings.objects.get(user=request.user)
        queryset = News.objects.filter(country_of_news__in=settings_obj.countries.values_list('name', flat=True),
                                       source_of_news__in=settings_obj.sources.values_list('name', flat=True))
        return queryset