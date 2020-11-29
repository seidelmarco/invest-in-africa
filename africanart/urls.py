from django.urls import path

from . import views

app_name = 'africanart'

urlpatterns = [
    path('', views.africanart, name='africanart'),
]