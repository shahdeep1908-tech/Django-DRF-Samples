from django.urls import path

from . import views

urlpatterns = [
    path('', views.DrinkList.as_view(), name='drink-list'),
    path('<int:id>', views.DrinkDetails.as_view(), name='drink-detail'),
]
