from django.config.urls import url
from . import views

app_name = 'categories'

urlpatterns = [
    url(r'^list/$', views.CategoryListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name='detail'),
    url(r'^search/$', views.CategorySearchView.as_view(), name='search'),
]