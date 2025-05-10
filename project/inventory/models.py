from django.db import models

# Create your models here.

class StockItem(models.Model):
    item_code=models.CharField(max_length=100,unique=True)
    description=models.TextField(max_length=100,default='d')
    unit_cost=models.DecimalField(decimal_places=2,max_digits=100)
    quantity_in_stock=models.IntegerField()
    reorder_level=models.IntegerField()
    
    def  __str__(self):
        return f"{self.item_code} {self.description} {self.unit_cost}{self.quantity_in_stock}{self.reorder_level}"
    
    
    
  