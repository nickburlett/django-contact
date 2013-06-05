from django.conf.urls import patterns, url
from .views import ContactListView

urlpatterns = patterns(
    '',
    url('^$', ContactListView.as_view(), name='contact-list'),
)
