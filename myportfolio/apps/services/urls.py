from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'services'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^list/$',views.ServiceListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.ServiceDetailView.as_view(),name='detail'),
    url(r'^search/$',views.ServiceSearchView.as_view(),name='search'),
]
