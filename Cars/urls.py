from django.urls import path
from  . import views

urlpatterns = [
    path('details/<int:id>/',views.CarDetails.as_view(),name='details'),
    path('buy/<int:car_id>/', views.buy, name='buy'),
]