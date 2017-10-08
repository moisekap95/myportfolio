from django.conf.urls import url,include
from . import views

# SET THE NAMESPACE!
app_name = 'core'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sendEmail/$',views.send_email_view,name='email'),
]
