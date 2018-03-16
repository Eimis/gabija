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
