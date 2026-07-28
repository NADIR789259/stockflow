from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from accounts.decorators import owner_required
from .models import PurchaseOrder, SalesOrder
from .forms import PurchaseOrderForm, SalesOrderForm


@login_required
def order_list(request):
    return render(request, "orders/order_list.html", {
        "purchase_orders": PurchaseOrder.objects.select_related("product", "supplier").order_by("-ordered_at"),
        "sales_orders": SalesOrder.objects.select_related("product").order_by("-ordered_at"),
    })


@owner_required
def purchase_order_create(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Purchase order recorded — stock updated.")
            return redirect("order_list")
    else:
        form = PurchaseOrderForm()
    return render(request, "orders/purchase_order_form.html", {"form": form})


@login_required
def sales_order_create(request):
    if request.method == "POST":
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sales order recorded — stock updated.")
            return redirect("order_list")
    else:
        form = SalesOrderForm()
    return render(request, "orders/sales_order_form.html", {"form": form})


@login_required
def sales_order_invoice(request, pk):
    order = get_object_or_404(SalesOrder, pk=pk)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="invoice_SO-{order.pk}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 18)
    p.drawString(50, height - 50, settings.APP_NAME)

    p.setFont("Helvetica", 10)
    p.drawString(50, height - 68, settings.APP_TAGLINE)

    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, height - 110, f"Invoice #SO-{order.pk}")

    p.setFont("Helvetica", 11)
    p.drawString(50, height - 135, f"Date: {order.ordered_at.strftime('%d %b %Y')}")
    p.drawString(50, height - 152, f"Customer: {order.customer_name or 'N/A'}")

    y = height - 195
    p.setFont("Helvetica-Bold", 11)
    p.drawString(50, y, "Product")
    p.drawString(280, y, "Quantity")
    p.drawString(380, y, "Unit Price")
    p.drawString(470, y, "Total")

    total = order.quantity * order.unit_price
    y -= 20
    p.setFont("Helvetica", 11)
    p.drawString(50, y, order.product.name)
    p.drawString(280, y, str(order.quantity))
    p.drawString(380, y, f"Rs. {order.unit_price}")
    p.drawString(470, y, f"Rs. {total}")

    y -= 35
    p.setFont("Helvetica-Bold", 12)
    p.drawString(380, y, "Grand Total:")
    p.drawString(470, y, f"Rs. {total}")

    p.showPage()
    p.save()
    return response
