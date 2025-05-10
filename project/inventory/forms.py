from django import forms
from.models import StockItem

class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = ('item_code', 'description','unit_cost','quantity_in_stock','reorder_level')
        
       