from django.urls import path

from . import views

urlpatterns = [
    path('', views.drink_list, name='drink-list'),
    path('<int:id>', views.drink_detail, name='drink-detail'),
]
