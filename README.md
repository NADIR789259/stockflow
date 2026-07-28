# StockFlow

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Track Stock. Fulfill Orders. Never Run Out.**

A full-stack inventory and order management system built with Django —
the kind of internal tool a small retail shop or warehouse would actually
use day-to-day, not another to-do app.

## Why I built this

I wanted to learn Django by shipping something real instead of following
a tutorial end-to-end. StockFlow started as a way to practice models,
the ORM, and Django's request/response cycle, and turned into a genuine
inventory system: stock that updates itself the moment an order is
placed, a dashboard that flags what needs reordering before it runs out,
role-based access so staff and owners see different things, and PDF
invoices generated on the fly. It's the project I'd point to if someone
asked "can you actually build something with Django, not just follow
along?"

## Screenshots

| Login | Products |
|---|---|
| <img width="1920" height="867" alt="Login" src="https://github.com/user-attachments/assets/2da3b4de-2230-4d44-b0e4-c28c5c781661" /> | <img width="1920" height="881" alt="Products" src="https://github.com/user-attachments/assets/04477672-a141-4152-a4e9-e05f9effca67" /> |

| Orders | Low Stock Dashboard |
|---|---|
| <img width="1920" height="881" alt="Orders" src="https://github.com/user-attachments/assets/2d0e72dc-7a15-43a6-a729-de6e3270ffaa" /> | <img width="1920" height="898" alt="Low Stock Products" src="https://github.com/user-attachments/assets/cb1d89b4-dd39-4020-b68e-c96f38f07063" /> |

**Sales Report**

<img width="1920" height="869" alt="Sales Reports" src="https://github.com/user-attachments/assets/00459f79-25f6-4db0-9580-2f833de359d9" />

## Features

- **Product catalog** — categories, SKUs, pricing, and live stock levels
- **Supplier management**
- **Purchase & Sales orders** with stock that adjusts itself automatically via Django signals
- **Overselling protection** — a sale can never exceed what's actually in stock
- **Low-stock dashboard** — see what needs reordering at a glance
- **Sales report** — 30-day revenue and top-selling products, computed with Django's ORM aggregation
- **PDF invoices**, generated on demand for every sale (ReportLab)
- **Role-based access** — Owner and Staff see and can do different things
- **Fully responsive UI** — Bootstrap 5, works on desktop, tablet, and phone

## Roles & Permissions

| Action | Owner | Staff |
|---|:---:|:---:|
| View products & orders | ✅ | ✅ |
| Add / edit products | ✅ | ❌ |
| Create a purchase order | ✅ | ❌ |
| Create a sales order | ✅ | ✅ |
| View low-stock dashboard & sales report | ✅ | ❌ |

An **Owner** is any Django superuser, or any user in the `Owner` group.
A **Staff** account is created by an Owner and added to the `Staff` group —
see [Setup](#setup) below.

## Tech Stack

- **Backend:** Django 5.2, Python 3.11+
- **Database:** PostgreSQL
- **Frontend:** Django Templates + Bootstrap 5
- **PDF generation:** ReportLab
- **Config:** python-dotenv — no secrets in source control

## Project Structure

```
stockflow/
├── accounts/       # Owner/Staff groups + permission decorator
├── products/       # Category & Product models, catalog CRUD
├── suppliers/      # Supplier model (managed via Django Admin)
├── orders/         # PurchaseOrder & SalesOrder, stock signals, PDF invoices
├── reports/        # Low-stock dashboard, sales report
├── templates/      # Shared base template + per-app templates
└── config/         # Settings, URLs, context processor
```

## Setup

```bash
git clone <your-repo-url>
cd stockflow

python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a PostgreSQL database:
```sql
CREATE DATABASE stockflow;
```

Create a `.env` file in the project root:
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

Generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Then:
```bash
python manage.py migrate      # also creates the Owner/Staff groups
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and log in.

### Creating a Staff account

Log in as Owner at `/admin/`, go to **Users → Add user**, leave "Staff
status" unchecked so they can't reach `/admin/`, then add them to the
`Staff` group. They can now log in at `/login/` with view-only access
plus the ability to record sales.

## What's Next

- Barcode scanning for stock updates
- Multi-location / multi-warehouse inventory
- Export reports to Excel
- Demand forecasting using historical sales data
- Payment gateway integration

## License

MIT — built as a personal portfolio project. Feel free to fork it and
make it your own.
