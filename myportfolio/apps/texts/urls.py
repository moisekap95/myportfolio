from django.conf.urls import url
from . import views

# SET THE NAMESPACE!
app_name = 'texts'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^list/$',views.TextListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.TextDetailView.as_view(),name='detail'),
    url(r'^search/$',views.TextSearchView.as_view(),name='search'),
]
