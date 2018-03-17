from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class ShoppingItem(models.Model):
    name = models.CharField(max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)
    # is the item already purchased?:
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.name
