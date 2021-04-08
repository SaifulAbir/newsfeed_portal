from django.db import IntegrityError
from rest_framework import status, serializers
from rest_framework.generics import CreateAPIView, get_object_or_404, \
    RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from newsfeed_portal.models import populate_user_info, populate_user_info_querydict
from settings.models import Settings, Country, Source, Keyword
from settings.serializers import SettingsSerializer, SettingsDetailSerializer
from rest_framework.utils import json


class SettingsCreateAPI(CreateAPIView):
    permission_classes = (IsAuthenticated,)
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

        try:
            settings_obj = Settings(user_id=request.user.id)
            populate_user_info(request, settings_obj, False)
            settings_obj.save()
        except IntegrityError:
            raise serializers.ValidationError("You have already added some information in your settings. Please update your settings.")

        if countries:
            country_list = countries.split(',')
            for country in country_list:
                country = country.strip()
                try:
                    country_obj = Country.objects.get(name=country)
                except Country.DoesNotExist:
                    country_obj = Country(name=country)
                    country_obj.save()
                if country_obj:
                    settings_obj.countries.add(country_obj)

        if sources:
            source_list = sources.split(',')
            for source in source_list:
                source = source.strip()
                try:
                    source_obj = Source.objects.get(name=source)
                except Source.DoesNotExist:
                    source_obj = Source(name=source)
                    source_obj.save()
                if source_obj:
                    settings_obj.sources.add(source_obj)

        if keywords:
            keyword_list = keywords.split(',')
            for keyword in keyword_list:
                keyword = keyword.strip()
                try:
                    keyword_obj = Keyword.objects.get(name=keyword)
                except Keyword.DoesNotExist:
                    keyword_obj = Keyword(name=keyword)
                    keyword_obj.save()
                if keyword_obj:
                    settings_obj.keywords.add(keyword_obj)
        data = SettingsDetailSerializer(settings_obj, many=False).data
        return Response(data, status=status.HTTP_201_CREATED)


class SettingsUpdateAPI(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SettingsSerializer

    def get_object(self):
        return get_object_or_404(Settings, user=self.request.user)

    def put(self, request, *args, **kwargs):
        req_data = request.data.copy()
        populate_user_info_querydict(request, req_data, True)
        print(req_data['countries'])
        try:
            countries = req_data['countries']
        except KeyError:
            countries = None

        try:
            sources = req_data['sources']
        except KeyError:
            sources = None

        try:
            keywords = req_data['keywords']
        except KeyError:
            keywords = None

        instance = self.get_object()
        country_list = []
        source_list = []
        keyword_list = []

        if countries:
            country_data = countries.split(',')
            for country in country_data:
                country = country.strip()
                try:
                    country_obj = Country.objects.get(name=country)
                except Country.DoesNotExist:
                    country_obj = Country(name=country)
                    country_obj.save()
                if country_obj:
                    country_list.append(country_obj.id)

        if sources:
            source_data = sources.split(',')
            for source in source_data:
                source = source.strip()
                try:
                    source_obj = Source.objects.get(name=source)
                except Source.DoesNotExist:
                    source_obj = Source(name=source)
                    source_obj.save()
                if source_obj:
                    source_list.append(source_obj.id)

        if keywords:
            keyword_data = keywords.split(',')
            for keyword in keyword_data:
                keyword = keyword.strip()
                try:
                    keyword_obj = Keyword.objects.get(name=keyword)
                except Keyword.DoesNotExist:
                    keyword_obj = Keyword(name=keyword)
                    keyword_obj.save()
                if keyword_obj:
                    keyword_list.append(keyword_obj.id)

        req_data['countries'] = country_list
        req_data['sources'] = source_list
        req_data['keywords'] = keyword_list
        serializer = self.get_serializer(instance, data=req_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = SettingsDetailSerializer(instance, many=False).data
        return Response(data)


class SettingsDetailAPI(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SettingsDetailSerializer

    def get_object(self):
        return get_object_or_404(Settings, user=self.request.user)