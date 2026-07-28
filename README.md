# StockFlow

**Track Stock. Fulfill Orders. Never Run Out.**

StockFlow is a full-stack inventory and order management system built with
Django. It replaces manual, spreadsheet-based stock tracking with a
centralized system that automatically adjusts stock levels on every
purchase or sale, flags products before they run out, and generates
professional PDF invoices — all behind role-based access control.

## Features

- **Product catalog** — categories, SKUs, pricing, and stock levels
- **Supplier management**
- **Purchase & Sales orders** with automatic stock adjustment via Django signals
- **Overselling protection** — a sale can't exceed available stock
- **Low-stock dashboard** — see what needs reordering at a glance
- **Sales report** — 30-day revenue and top-selling products
- **PDF invoice generation** for every sale (ReportLab)
- **Role-based access** — Owner and Staff roles with different permissions
- **Responsive UI** built with Bootstrap 5 — works on desktop, tablet, and mobile

## Roles & Permissions

| Action | Owner | Staff |
|---|---|---|
| View products & orders | ✅ | ✅ |
| Add / edit products | ✅ | ❌ |
| Create a purchase order | ✅ | ❌ |
| Create a sales order | ✅ | ✅ |
| View low-stock dashboard & sales report | ✅ | ❌ |

An **Owner** is any Django superuser, or any user added to the `Owner` group.
A **Staff** user is added to the `Staff` group (see Setup below).

## Tech Stack

- **Backend:** Django 5.2, Python 3.11+
- **Database:** PostgreSQL
- **Frontend:** Django Templates + Bootstrap 5 (CDN)
- **PDF generation:** ReportLab
- **Config:** python-dotenv (secrets kept out of source control)

## Project Structure

```
stockflow/
├── accounts/       # Owner/Staff groups + permission decorator
├── products/       # Category & Product models, catalog CRUD
├── suppliers/      # Supplier model (managed via Django Admin)
├── orders/         # PurchaseOrder & SalesOrder, stock-adjustment signals, PDF invoices
├── reports/        # Low-stock dashboard, sales report
├── templates/       # Shared base template + per-app templates
└── config/         # Project settings, URLs, context processor
```

## Setup

1. **Clone and enter the project**
   ```bash
   git clone <your-repo-url>
   cd stockflow
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux

   pip install -r requirements.txt
   ```

3. **Create a PostgreSQL database**
   ```sql
   CREATE DATABASE stockflow;
   ```

4. **Create a `.env` file** in the project root:
   ```env
   DB_NAME=stockflow
   DB_USER=postgres
   DB_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_PORT=5432

   SECRET_KEY=generate-your-own-secret-key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   ```
   Generate a secret key with:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Run migrations** (this also creates the `Owner` and `Staff` groups automatically)
   ```bash
   python manage.py migrate
   ```

6. **Create your Owner account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` and log in.

### Creating a Staff user

Log in as Owner at `/admin/`, go to **Users → Add user**, create the account,
leave "Staff status" unchecked (so they can't reach `/admin/`), then under
**Groups** add them to `Staff`. They can now log in at `/login/` with access
limited to viewing products/orders and creating sales orders.

## Future Improvements

- Barcode scanning for stock updates
- Multi-location / multi-warehouse inventory
- Export reports to Excel
- ML-based restock/demand forecasting
- Payment gateway integration for online orders

## License

This project was built as a personal portfolio project.
