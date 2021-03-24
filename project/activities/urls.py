from django.urls import path
from .views import ActivitiesListView

urlpatterns = [
    path("", ActivitiesListView.as_view(), name="activities_list"),
]
