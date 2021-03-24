from django.shortcuts import render
from django.views.generic import ListView

from .models import Activity

class ActivitiesListView(ListView):
    model = Activity
    context_object_name = "activities"
    template_name = "activities/activities_list.html"