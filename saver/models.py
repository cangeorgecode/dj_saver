from django.db import models
from django.contrib.auth.models import User

class Saving(models.Model):
    item_name = models.CharField(max_length=50)
    item_cost = models.IntegerField()
    item_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_name
