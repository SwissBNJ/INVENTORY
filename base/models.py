from django.db import models

# Create your models here.
class Item(models.Model):
    
    item_name = models.CharField(max_length = 200)
    item_price = models.CharField(max_length = 200)
    item_quantity = models.CharField(max_length = 200)
    
    def __str__(self) -> str:
        return self.item_name