from django.contrib import admin
from django.urls import path, include

# Project urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saver.urls')),
    path('membership/', include('membership.urls')),
]
