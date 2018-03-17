from django.core.urlresolvers import reverse
from django.test import TestCase

from gabija.models import ShoppingItem


class GroceriesAPITestCase(TestCase):

    def test_main_view(self):
        """
        Tests if main app view returns proper status code
        """

        url = reverse('main')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_shopping_item_view(self):
        """
        Tests if this API endpoint creates a ShoppingItem model instance
        """
        items_before = ShoppingItem.objects.count()

        post_data = {'shopping_item': 'Apple'}

        response = self.client.post(
            reverse('create_shopping_item'),
            post_data,
        )
        items_after = ShoppingItem.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(items_after, items_before + 1)

        new_item = ShoppingItem.objects.get(name=post_data['shopping_item'])

        # Was new item created:
        self.assertEqual(new_item.name, post_data['shopping_item'])
        self.assertEqual(new_item.purchased, False)

        # Check response data:
        self.assertEqual(response.data['name'], post_data['shopping_item'])
        self.assertEqual(response.data['purchased'], False)
