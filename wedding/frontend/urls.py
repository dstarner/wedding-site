from django.urls import path

from . import views


urlpatterns = [
    path('', views.rsvp_index),
    path('party/<str:code>', views.rsvp_party, name='rsvp-party'),
    path('party/<str:code>/guests', views.rsvp_guests, name='rsvp-guests'),
    path('party/<str:code>/decline', views.decline, name='decline'),
]