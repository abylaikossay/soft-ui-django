from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from home.models import ConsumerExistingPosition


# Traders list
def index(request):
    assert isinstance(request, HttpRequest)
    positions = ConsumerExistingPosition.objects.all()
    print(positions)
    return render(
        request,
        'pages/consumer_positions/index.html',
        {
            'positions': positions,
            'type': 'EXISTING'
        }
    )