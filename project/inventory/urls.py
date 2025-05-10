from django.urls import path
from.views import add_stock_item,stock_item_list

urlpatterns = [
    path('add/', add_stock_item, name='add'),
    path('stock/', stock_item_list, name='stock_item_list'),
]
