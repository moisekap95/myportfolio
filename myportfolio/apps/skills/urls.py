from django.config.urls import url
from . import views

app_name = 'skills'

urlpatterns = [
    url(r'^list/$',views.SkillListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.SkillDetailView.as_view(),name='detail'),
    url(r'^search/$',views.SkillSearchView.as_view(),name='search'),
]