from django.urls import path 

from .views import homepageview, coinview

urlpatterns = [
    path('', homepageview, name='homepagaview'),
    path('coin/<coin_name>', coinview, name='coinview'),
]