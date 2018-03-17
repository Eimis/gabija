from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from gabija.models import ShoppingItem
from gabija.serializers import ShoppingItemSerializer


def main(request):
    '''Main app view for SPA
    '''

    return render(request, 'main.html', {})


class CreateShoppingItemView(APIView):
    """
    View to create a shopping item in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    # ony allow POST request:
    http_method_names = ['post', ]

    def post(self, request, format=None):
        """
        Create a ShoppingItem instance.
        """
        item = request.data.get('shopping_item', None)

        if not item:
            return Response(status=403)

        new_item = ShoppingItem.objects.create(name=item)
        serializer = ShoppingItemSerializer(new_item)

        return Response(serializer.data)


class ListShoppingItemsView(APIView):
    """
    View to list all shopping items in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    # ony allow GET request:
    http_method_names = ['get', ]

    def get(self, request, format=None):
        """
        Lists all ShoppingItem instances.
        """
        items = ShoppingItem.objects.all()
        serializer = ShoppingItemSerializer(items, many=True)

        return Response(serializer.data)


class ClearShoppingItemsView(APIView):
    """
    View to clear all shopping items in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    # ony allow GET request:
    http_method_names = ['get', ]

    def get(self, request, format=None):
        """
        Clears all ShoppingItem instances.
        """
        items = ShoppingItem.objects.all()
        items.delete()

        return Response({'ok': True})

class UpdateShoppingItemView(APIView):
    """
    View to update shopping item instance in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    # ony allow POST request:
    http_method_names = ['post', ]

    def post(self, request, format=None):
        """
        Update a ShoppingItem instance.
        """
        item = request.data.get('updated_item', None)

        # Safety:
        if not item:
            return Response(status=403)

        if 'purchased' not in item.keys() or 'name' not in item.keys():
            return Response(status=403)

        name = item['name']
        purchased = item['purchased']

        item_to_update = ShoppingItem.objects.filter(name=name).first()

        if item_to_update:
            item_to_update.purchased = purchased
            item_to_update.save()

            serializer = ShoppingItemSerializer(item_to_update)

            return Response(serializer.data)
        else:
            return Response(status=403)


class SyncShoppingItemsView(APIView):
    """
    View to sync database with items when switching to online mode from
    frontend.

    * Requires no authentication
    * Requires no special permissions
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    # ony allow POST request:
    http_method_names = ['post', ]

    def post(self, request, format=None):
        """
        Sync ShoppingItem instances.
        """
        posted_items = request.data.get('items', None)

        current_items = ShoppingItem.objects.all()
        posted_item_names = [item['name'] for item in posted_items]

        # 1. remove items from database that have been deleted in offline mode:
        for item in current_items:
            if item.name not in posted_item_names:
                item.delete()

        # 2. create items that are not yet present in the database and that
        # have been created in offline mode. Also, update 'purchased' states:
        for item in posted_items:
            try:
                i = ShoppingItem.objects.get(name=item['name'])
                i.purchased = item['purchased']
                i.save()
            except ShoppingItem.DoesNotExist:
                ShoppingItem.objects.create(
                    name=item['name'],
                    added_on=item['added_on'],
                    purchased=item['purchased'],
                )

        return Response({'ok': True})
