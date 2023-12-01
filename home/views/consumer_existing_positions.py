from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
import requests
from home.models import ConsumerExistingPosition, Trader


# Traders list
def index(request):
    assert isinstance(request, HttpRequest)
    positions = ConsumerExistingPosition.objects.all()
    consumers = Trader.objects.filter(is_consumer=True)
    print(positions)
    print(consumers)
    return render(
        request,
        'pages/consumer_positions/index.html',
        {
            'positions': positions,
            'consumers': consumers,
            'type': 'EXISTING'
        }
    )


def refresh_positions(request, consumer_id):
    assert isinstance(request, HttpRequest)
    print(consumer_id)
    print("Send Refresh API REQUEST")
    api_url = f"https://position-manager-production.up.railway.app/reload_positions/{consumer_id}"
    response = requests.get(api_url)
    if response.ok:
        print("Send Refresh API REQUEST successful")
    else:
        print(f"Failed to send Refresh API REQUEST. Status code: {response.status_code}")
    return redirect('consumer_existing_positions_index')
