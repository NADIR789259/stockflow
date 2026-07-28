from django import forms
from accounts.forms import BootstrapFormMixin
from .models import PurchaseOrder, SalesOrder


class PurchaseOrderForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'product', 'quantity', 'unit_cost']


class SalesOrderForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['product', 'quantity', 'unit_price', 'customer_name']
