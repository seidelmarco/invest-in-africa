from . import views
from django.urls import path


# hier kein Namespacing <app_name = 'blog'> einsetzen, weil die Templates für blog als Hauptanwendung im base-root
# liegen.


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/draft/', views.PostDrafts.as_view(), name='post_drafts'),
]
