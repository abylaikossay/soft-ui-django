from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from home.models import ProviderExistingPosition


# Traders list
def index(request):
    assert isinstance(request, HttpRequest)
    positions = ProviderExistingPosition.objects.all()
    print(positions)
    return render(
        request,
        'pages/producer_positions/index.html',
        {
            'positions': positions,
            'type': 'EXISTING'
        }
    )