from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from accounts.forms import StyledAuthenticationForm

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="product_list", permanent=False)),
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=StyledAuthenticationForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("products/", include("products.urls")),
    path("orders/", include("orders.urls")),
    path("reports/", include("reports.urls")),
]
