from django.shortcuts import render,redirect
from.models import StockItem
from.forms import StockItemForm
# Create your views here.

def add_stock_item(request):
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_item_list')
    else:
        form = StockItemForm()
    return render(request, 'add_stock_item.html', {'form': form})

def  stock_item_list(request):
    stock = StockItem.objects.all()
    return render(request,'stock_item_list.html',{'stock':stock})
    
    