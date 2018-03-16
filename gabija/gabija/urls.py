from django.conf.urls import url
from django.contrib import admin

from gabija.views import CreateShoppingItemView, main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(
        r'^shopping/create$',
        CreateShoppingItemView.as_view(),
        name='create_shopping_item'
    ),
]
