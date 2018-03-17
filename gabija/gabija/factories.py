import factory.django

from gabija.models import ShoppingItem


class ShoppingItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ShoppingItem
