from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from home.models import ConsumerTargetPosition


# Traders list
def index(request):
    assert isinstance(request, HttpRequest)
    positions = ConsumerTargetPosition.objects.all()
    print(positions)
    print("Show target Positions")
    return render(
        request,
        'pages/consumer_positions/index.html',
        {
            'positions': positions,
            'type': 'TARGET'
        }
    )