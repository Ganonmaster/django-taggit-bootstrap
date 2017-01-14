from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', TaggitBoostrapView.as_view(), name='taggit-bootstrap')
]
