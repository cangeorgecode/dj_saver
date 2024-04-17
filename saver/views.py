from django.shortcuts import render, redirect
import datetime
from .models import Saving
from django.db.models import Sum
from .forms import SavingForm
from django.contrib import messages
# from django import forms
import time

def index(request):
    cur_year = datetime.datetime.now().strftime("%Y")
    context = {
        'cur_year': cur_year,
    }
    return render(request, 'saver/index.html', context)
        
def viewitem(request): # list and create
    if request.user.is_authenticated:
        form = SavingForm()
        items = Saving.objects.filter(item_owner=request.user)
        total_saved = items.aggregate(Sum('item_cost'))
        context = {
            'form': form,
            'items': items,
            'total_saved': total_saved,
        }
        if request.method == "POST":
            form = SavingForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.item_owner = request.user
                instance.save()
                messages.success(request, 'New item successfully added')
                time.sleep(1)
                return redirect('viewitem')
            else:
                form = SavingForm()
                messages.success(request, 'There is an error. Please try again.')
                return render(request, 'saver/viewitem.html', context)
    return render(request, 'saver/viewitem.html', context)

def viewitemdetails(request, item_id): # update
    if request.user.is_authenticated:
        items = Saving.objects.get(pk=item_id)
        form = SavingForm(instance=items)
        if request.method == "POST":
            form = SavingForm(request.POST, instance=items)
            if form.is_valid():
                form.save()
                messages.success(request, 'Item has been updated')
                return redirect('viewitem')
            else:
                form = SavingForm(instance=items)
                messages.success(request, 'There was an error. Please try again')
                return render(request, 'saver/viewitemdetails.html', {'form': form})
        return render(request, 'saver/viewitemdetails.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to see this')
        return redirect(request, 'saver/index.html', {})
    

def deleteitem(request, item_id):
    if request.user.is_authenticated:
        item = Saving.objects.get(pk=item_id)
        item.delete()
        messages.success(request, 'Item has been deleted')
        return redirect('viewitem')