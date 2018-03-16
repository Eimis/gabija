from django.db import models


class ShoppingItem(models.Model):
    name = models.CharField(max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)
