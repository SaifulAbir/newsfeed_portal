from django.urls import path
from settings.api import SettingsCreateAPI, SettingsUpdateAPI, SettingsDetailAPI

urlpatterns = [
    path('settings/create/', SettingsCreateAPI.as_view()),
    path('settings/update/', SettingsUpdateAPI.as_view()),
    path('settings/details/', SettingsDetailAPI.as_view()),
]