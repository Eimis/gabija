from django.conf.urls import url
from django.contrib import admin

from gabija.views import CreateShoppingItemView, ClearShoppingItemsView, \
    ListShoppingItemsView, main, UpdateShoppingItemView

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
    url(
        r'^shopping/clear$',
        ClearShoppingItemsView.as_view(),
        name='clear_shopping_items'
    ),
    url(
        r'^shopping/update$',
        UpdateShoppingItemView.as_view(),
        name='update_shopping_item'
    ),
]
