from django.conf.urls import url
from django.contrib import admin

from gabija.views import main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
]
