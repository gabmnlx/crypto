from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('appcrypto.urls')),
    path('admin/', admin.site.urls),
]
