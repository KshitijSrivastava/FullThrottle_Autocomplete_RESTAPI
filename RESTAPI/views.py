from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Welcomes the user to the REST API
    """
    return HttpResponse('Welcome to REST API')
