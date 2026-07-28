from django.contrib import admin
from .models import PurchaseOrder, SalesOrder

# Register your models here.

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "supplier", "quantity", "unit_cost", "ordered_at")


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "customer_name", "quantity", "unit_price", "ordered_at")
