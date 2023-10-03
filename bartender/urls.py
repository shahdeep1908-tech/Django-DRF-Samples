from django.urls import path
from . import views

urlpatterns = [
    path('', views.BartenderList.as_view(), name='bartender-list'),
    path('<int:pk>', views.BartenderDetails.as_view(), name='bartender-details'),
]
