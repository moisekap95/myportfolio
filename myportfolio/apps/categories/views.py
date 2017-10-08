from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView, FormView)
from . import models

from django.db.models import Q
from django.shortcuts import redirect, render

# Create your views here.

#CRUD Views

class CategoryListView(ListView):
    context_object_name = 'categories'
    model = models.Category

class CategoryDetailView(DetailView):
    context_object_name = 'category_details'
    model = models.Category
    template_name = 'categories/category_details.html'

class CategorySearchView(ListView):
    template_name = 'categories/search_result.html'
    model = models.Category
    context_object_name = 'categories'
    fieldsData = {}

    def get_queryset(self):
        #add fieldData to context dictionary
        self.fieldsData['name'] = self.request.GET['name']
        self.fieldsData['city'] = self.request.GET['city']
        self.fieldsData['state'] = self.request.GET['state']
        self.fieldsData['country'] = self.request.GET['country']

        name = self.request.GET['name']
        city = self.request.GET['city']
        state = self.request.GET['state']
        country = self.request.GET['country']

        if not self.model.objects.filter(city__icontains=city):
            city = ''
        if not self.model.objects.filter(state__icontains=state):
            state = ''
        if not self.model.objects.filter(country__icontains=country):
            country = ''

        return self.model.objects.filter(name__icontains=name, city__icontains=city, state__icontains=state, country__icontains=country)

    #def get_context_data(self,**kwargs):
        #context  = super().get_context_data(**kwargs)
        #congregation_search_form = forms.CongregationSearchForm()
        #context['congregation_search_form'] = congregation_search_form
        #context['fieldsData'] = self.fieldsData
        #return context
