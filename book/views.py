import csv
from django.shortcuts import render
from django.contrib import messages
from django. contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    return render(request, 'index.html')






