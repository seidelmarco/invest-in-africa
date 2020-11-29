from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def africanart(request):
    return render(request, 'africanart/africanart.html',)

