from django.urls import path
from fetchrewards.receipts import views

urlpatterns = [
    path('receipts/process', views.process_receipt),
    path('receipts/<int:id>/points', views.get_points)
]