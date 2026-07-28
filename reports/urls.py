from django.urls import path
from . import views

urlpatterns = [
    path('low-stock/', views.low_stock_dashboard, name='low_stock_dashboard'),
    path('sales/', views.sales_report, name='sales_report'),
]


