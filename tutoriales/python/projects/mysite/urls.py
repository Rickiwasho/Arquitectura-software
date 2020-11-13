from django.conf.urls import url
from django.contrib import admin
from django.urls import include, url

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
