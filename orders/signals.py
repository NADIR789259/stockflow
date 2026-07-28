from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import PurchaseOrder, SalesOrder


@receiver(post_save, sender=PurchaseOrder)
def increase_stock_on_purchase(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            product = instance.product
            product.stock_quantity += instance.quantity
            product.save()


@receiver(post_save, sender=SalesOrder)
def decrease_stock_on_sale(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            product = instance.product
            product.stock_quantity -= instance.quantity
            product.save()