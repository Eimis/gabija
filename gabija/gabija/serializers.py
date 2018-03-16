from rest_framework import serializers

from gabija.models import ShoppingItem


class ShoppingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingItem
        fields = ('name', 'added_on', )
