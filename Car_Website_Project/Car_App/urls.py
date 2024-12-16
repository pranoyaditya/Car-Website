from django.urls import path
from .views import CarDetails, BuyCarView

urlpatterns = [
    path('<int:pk>/', CarDetails.as_view(), name='car_details_page'),
    path('buy/<int:car_id>/', BuyCarView.as_view(), name='buy_car'),
]