from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, **kawrgs):
    status = kawrgs.get('status', 'No Other value is shown on app2')
    print(status)
    return HttpResponse(f'Hello World, <h3> {status} <h4/>')