from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'works'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^list/$',views.WorkListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.WorkDetailView.as_view(),name='detail'),
    url(r'^search/$',views.WorkSearchView.as_view(),name='search'),
]
