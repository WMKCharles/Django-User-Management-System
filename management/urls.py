from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls')),
    path('account/', include('users.urls')),
]
