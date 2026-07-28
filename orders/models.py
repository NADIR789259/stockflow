from django.db import models
from products.models import Product
from suppliers.models import Supplier
from django.core.exceptions import ValidationError


# Create your models here.

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name="purchase_orders")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="purchase_orders")
    quantity = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PO-{self.pk} | {self.product.name} x{self.quantity}"


class SalesOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="sales_orders")
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_name = models.CharField(max_length=200, blank=True)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.product_id and self.quantity > self.product.stock_quantity:
            raise ValidationError(
                f"Not enough stock. Available: {self.product.stock_quantity}, requested: {self.quantity}"
            )

    def __str__(self):
        return f"SO-{self.pk} | {self.product.name} x{self.quantity}"
    
