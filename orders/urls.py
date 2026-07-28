from django.urls import path
from . import views

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("purchase/add/", views.purchase_order_create, name="purchase_order_create"),
    path("sales/add/", views.sales_order_create, name="sales_order_create"),
    path("sales/<int:pk>/invoice/", views.sales_order_invoice, name="sales_order_invoice"),
]
