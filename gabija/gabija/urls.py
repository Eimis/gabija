from django.conf.urls import url
from django.contrib import admin

from gabija.views import CreateShoppingItemView, ListShoppingItemsView, main

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(
        r'^shopping/create$',
        CreateShoppingItemView.as_view(),
        name='create_shopping_item'
    ),
    url(
        r'^shopping/list$',
        ListShoppingItemsView.as_view(),
        name='list_shopping_items'
    ),
]
