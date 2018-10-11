from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GenderForm
from django.views.generic import ListView, CreateView, UpdateView
from . models import Gender, Diseases
from django.db.models import Count
from django.views.generic.list import ListView
from django.db.models import F


class CreateMyModelView(CreateView):
    model = Diseases
    form_class = GenderForm
    template_name = 'checkmate/name.html'
    success_url = '/checkmate/results'
    context_object_name = 'name'


class MyModelListView(ListView):
    template_name = 'checkmate/result.html'
    context_object_name = 'Results'

    def get_queryset(self):
        queryset = Diseases.objects.values(Gender=F('gender_disease__gender'), Diseases=F('diseases')).annotate(Patients=Count('*'))
        return queryset


