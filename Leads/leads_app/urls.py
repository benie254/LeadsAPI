from django.urls import path, re_path as url
from leads_app import views 

urlpatterns = [
    url(r'^contact/$',views.AllContacts.as_view(),name='contact'),
    url(r'^subscribe/$',views.AllSubscribers.as_view(),name='subscribe'),
]