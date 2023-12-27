from django.urls import path
from . import views

urlpatterns = [
    path('sponsors/', views.sponsors, name='sponsors'),
]