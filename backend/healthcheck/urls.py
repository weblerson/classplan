from django.urls import path
from .views import HealthcheckView
from django.http import HttpResponse


urlpatterns = [
    path('', lambda r: HttpResponse(), name='healthcheck')
]
