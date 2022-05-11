from django.urls import path

from . import views


urlpatterns = [
    path('', views.rsvp_index),
    path('party/<str:code>', views.rsvp_party, name='rsvp-party'),
]