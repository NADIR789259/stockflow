from django.shortcuts import render
from django.db.models import F, Sum
from django.utils import timezone
from datetime import timedelta

from accounts.decorators import owner_required
from products.models import Product
from orders.models import SalesOrder


@owner_required
def low_stock_dashboard(request):
    low_stock_products = Product.objects.select_related("category").filter(
        stock_quantity__lte=F("reorder_threshold")
    ).order_by("stock_quantity")
    return render(request, "reports/low_stock.html", {"products": low_stock_products})


@owner_required
def sales_report(request):
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)

    orders_in_range = SalesOrder.objects.filter(
        ordered_at__date__gte=start_date,
        ordered_at__date__lte=end_date,
    )

    total_revenue = orders_in_range.aggregate(
        total=Sum(F("quantity") * F("unit_price"))
    )["total"] or 0

    top_products = (
        orders_in_range
        .values("product__name")
        .annotate(total_sold=Sum("quantity"))
        .order_by("-total_sold")[:5]
    )

    return render(request, "reports/sales_report.html", {
        "start_date": start_date,
        "end_date": end_date,
        "total_revenue": total_revenue,
        "top_products": top_products,
    })
