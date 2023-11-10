from django.urls import path
from .views import HealthcheckView


urlpatterns = [
    path('', HealthcheckView.as_view(), name='healthcheck')
]
