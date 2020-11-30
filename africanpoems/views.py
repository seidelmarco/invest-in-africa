from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def africanpoems(request):
    return render(request, 'africanpoems/africanpoems.html',)