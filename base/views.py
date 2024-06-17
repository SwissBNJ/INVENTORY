from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.

def homepage(request):
    items = Item.objects.all()
    return render(request, 'home_page.html', {'items': items})

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id) 
    item.delete()
    return redirect('homepage')


def update_item_form(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item_name' : item.item_name , 'item_price' : item.item_price , 'item_quantity' : item.item_quantity}
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ItemForm(instance=item)
    context['form'] = form
    return render(request, 'update_item_form.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})
