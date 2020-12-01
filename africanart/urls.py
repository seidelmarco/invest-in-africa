from django.urls import path

from . import views

app_name = 'africanart'

urlpatterns = [
    path('', views.africanart, name='africanart'),
    path('picture_gallery/', views.picture_gallery, name='picture_gallery'),
]

