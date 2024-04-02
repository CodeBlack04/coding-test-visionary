from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('add/', views.add_movie, name='add'),
    path('<str:id>/', views.detail, name='detail'),
    path('<str:id>/edit/', views.edit_movie, name='edit'),
    path('<str:id>/delete/', views.delete_movie, name='delete'),
]