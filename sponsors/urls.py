from django.urls import path
from . import views

urlpatterns = [
    path('sponsors/', views.sponsors, name='sponsors'),
    path('sponsors/details/<int:id>', views.details, name='details')
]