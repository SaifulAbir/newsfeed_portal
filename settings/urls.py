from django.urls import path
from settings.api import SettingsCreateAPI, SettingsUpdateAPI

urlpatterns = [
    path('settings/create/', SettingsCreateAPI.as_view()),
    path('settings/update/<str:pk>/', SettingsUpdateAPI.as_view()),
]