from django.urls import path

from . import views

app_name = 'dataproject'

urlpatterns = [
    path('', views.index, name='index'),
]