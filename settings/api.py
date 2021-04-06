from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from newsfeed_portal.models import populate_user_info
from settings.models import Settings, Country, Source, Keyword
from settings.serializers import SettingsSerializer
from rest_framework.utils import json


class SettingsCreateAPI(CreateAPIView):
    serializer_class = SettingsSerializer

    def post(self, request, *args, **kwargs):
        settings_data = json.loads(request.body)

        try:
            countries = settings_data['countries']
        except KeyError:
            countries = None

        try:
            sources = settings_data['sources']
        except KeyError:
            sources = None

        try:
            keywords = settings_data['keywords']
        except KeyError:
            keywords = None

        settings_obj = Settings(user_id=request.user.id)
        populate_user_info(request, settings_obj, False)
        settings_obj.save()

        if countries:
            country_list = countries.split(',')
            for country in country_list:
                try:
                    country_obj = Country.objects.get(name=country)
                except Country.DoesNotExist:
                    country_obj = Country(name=country)
                if country_obj:
                    settings_obj.countries.add(country_obj)

        if sources:
            source_list = sources.split(',')
            for source in source_list:
                try:
                    source_obj = Source.objects.get(name=source)
                except Source.DoesNotExist:
                    source_obj = Source(name=source)
                if source_obj:
                    settings_obj.sources.add(source_obj)

        if keywords:
            keyword_list = keywords.split(',')
            for keyword in keyword_list:
                try:
                    keyword_obj = Keyword.objects.get(name=keyword)
                except Keyword.DoesNotExist:
                    keyword_obj = Keyword(name=keyword)
                if keyword_obj:
                    settings_obj.keywords.add(keyword_obj)

        return Response(HTTP_200_OK)