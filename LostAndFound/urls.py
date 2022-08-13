from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('lostlist/', include('lostlist.urls')),
    path('admin/', admin.site.urls),
]
