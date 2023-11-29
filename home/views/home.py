from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pages/index.html'
    )


@require_http_methods(["GET"])
def health_check(request):
    return JsonResponse({'status': 'OK'})
