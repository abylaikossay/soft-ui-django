from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from home.models import Trader
from home.forms import TraderForm


# Traders list
def index(request):
    assert isinstance(request, HttpRequest)
    traders = Trader.objects.all()
    print(traders)
    return render(
        request,
        'pages/traders/index.html',
        {
            'traders': traders,
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        form = TraderForm
    return render(
        request,
        'pages/traders/add.html',
        {
            'form': form
        }
    )

def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = TraderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Trader has been saved successfully !")
        else:
            print(form.errors)
            messages.error(request, "Error occurred while saving trader !")

        return redirect('/traders')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = TraderForm()
        else:
            trader = Trader.objects.get(pk=id)
            form = TraderForm(instance=trader)
        return render(
            request,
            'pages/traders/edit.html',
            {
                'form': form
            }
        )


# Remove a trader
def delete(request, id):
    trader = Trader.objects.get(pk=id)
    trader.delete()
    messages.success(request, "Trader has been removed successfully !")
    return redirect('/traders')
