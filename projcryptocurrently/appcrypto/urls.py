from django.urls import path 

from .views import index, indexhtmlview

urlpatterns = [
    path('', index, name='index'),
    path('index', indexhtmlview, name='indexhtmlview')
]