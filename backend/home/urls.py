from django.urls import path
from .views import TaskCreationView

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),

    path('spaces/<int:space_id>/tasks/', TaskCreationView.as_view(), name='task_creation')
]
