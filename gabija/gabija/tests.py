from django.core.urlresolvers import reverse
from django.test import TestCase

from gabija.factories import ShoppingItemFactory
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

        response = self.client.post(reverse('create_shopping_item'), post_data)
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

    def test_list_shopping_items_view(self):
        """
        Tests if this API endpoint lists all ShoppingItem model instances
        """
        apple = ShoppingItemFactory(name='Apple')
        pear = ShoppingItemFactory(name='Pear')
        orange = ShoppingItemFactory(name='Orange')

        response = self.client.get(reverse('list_shopping_items'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

        self.assertEqual(response.data[0]['name'], apple.name)
        self.assertEqual(response.data[1]['name'], pear.name)
        self.assertEqual(response.data[2]['name'], orange.name)

        self.assertEqual(response.data[0]['purchased'], apple.purchased)
        self.assertEqual(response.data[1]['purchased'], pear.purchased)
        self.assertEqual(response.data[2]['purchased'], orange.purchased)

        # XXX: it's mpossible to test exact added_on response, because it's a
        # datetime field and converting response back to UTC creates a lot of
        # mess:
        self.assertTrue(response.data[0]['added_on'])
        self.assertTrue(response.data[1]['added_on'])
        self.assertTrue(response.data[2]['added_on'])

    def test_clear_shopping_items_view(self):
        """
        Tests if this API endpoint clears all ShoppingItem model instances
        """
        ShoppingItemFactory(name='Apple')
        ShoppingItemFactory(name='Pear')
        ShoppingItemFactory(name='Orange')

        self.assertEquals(ShoppingItem.objects.count(), 3)

        response = self.client.get(reverse('clear_shopping_items'))
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.data, {'ok': True})

        self.assertEquals(ShoppingItem.objects.count(), 0)
