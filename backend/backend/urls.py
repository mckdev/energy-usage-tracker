from django.conf.urls import include
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('tracker.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
