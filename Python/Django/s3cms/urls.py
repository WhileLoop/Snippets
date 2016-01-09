from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 's3cms'
urlpatterns = [
    url(r'^$', views.SalesItemListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.SalesItemDetailView.as_view(), name='detail'),
]
