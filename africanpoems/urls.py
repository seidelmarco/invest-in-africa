from django.urls import path

from . import views

app_name = 'africanpoems'

urlpatterns = [
    path('', views.africanpoems, name='africanpoems'),
]