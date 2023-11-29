from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from home.models import Trader, ConsumerState
from home.forms import TraderForm, ConsumerStateForm


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
            is_consumer = form.data.get('is_consumer')
            trader = form.save()
            messages.success(request, "Trader has been saved successfully !")
            # if is_consumer:
            #     consumer_state_form = ConsumerStateForm(initial={'consumer': trader.id})
            #
            #     print("THIS IS CONSUMER ADD SOME DATA ADDITIONALLY")
            #     return render(
            #         request,
            #         'pages/traders/add-state.html',
            #         {
            #             'form': consumer_state_form,
            #             'trader_id': trader.id
            #         }
            #     )
            # else:
            #     print("THIS IS PROVIDER")

        else:
            print(form.errors)
            messages.error(request, "Error occurred while saving trader !")

        return redirect('/traders')


def store_state(request):
    print("STORE STATE")
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = ConsumerStateForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, "Consumer state has been saved successfully !")
        else:
            print(form.errors)
            messages.error(request, "Error occurred while saving trader !")

        return redirect('/traders')


def add_state(request, id):
    assert isinstance(request, HttpRequest)

    trader = get_object_or_404(Trader, pk=id)

    # Check if the trader is a consumer
    if trader.is_consumer:
        # Try to get the existing ConsumerState instance for the trader
        consumer_state = ConsumerState.objects.filter(consumer_id=id).first()

        if consumer_state:
            # If a ConsumerState exists, display it for editing
            form = ConsumerStateForm(instance=consumer_state)
        else:
            # If no ConsumerState exists, create a new form for adding
            form = ConsumerStateForm(initial={'consumer': trader.id})

        return render(
            request,
            'pages/traders/add-state.html',
            {
                'form': form,
                'trader_id': trader.id
            }
        )
    else:
        # Handle the case where the trader is not a consumer
        # Redirect or display an error message
        return redirect('/traders')  # Redirect to traders page or customize this based on your logi


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


def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = TraderForm(request.POST)
        else:
            trader = Trader.objects.get(pk=id)
            form = TraderForm(request.POST, instance=trader)
        if form.is_valid():
            form.save()
        messages.success(request, "Trader has been updated successfully !")
        return redirect('/traders')


def update_store(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ConsumerStateForm(request.POST)
        else:
            consumerState = ConsumerState.objects.get(pk=id)
            form = ConsumerStateForm(request.POST, instance=consumerState)
        if form.is_valid():
            form.save()
        messages.success(request, "Consumer has been updated successfully !")
        return redirect('/traders')

# Remove a trader
def delete(request, id):
    trader = Trader.objects.get(pk=id)
    trader.delete()
    messages.success(request, "Trader has been removed successfully !")
    return redirect('/traders')
