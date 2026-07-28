from django import forms
from accounts.forms import BootstrapFormMixin
from .models import Product


class ProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'description', 'price', 'cost_price', 'stock_quantity', 'reorder_threshold']
