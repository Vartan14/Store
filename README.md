# Clothing Store

It's a web application for organizing the work of a clothing store. The backend is developed using Python and Django framework, PostgreSQL and Redis (caching) databases, Celery to implement delayed tasks.

![Django](https://img.shields.io/badge/Django-5.0.1-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.2-blue)
![Redis](https://img.shields.io/badge/Redis-5.0.1-red)
![Celery](https://img.shields.io/badge/Celery-5.3.6-green)
![OAuth2.0](https://img.shields.io/badge/OAuth2.0-Authorization-yellow)


## Description

**Store** is a comprehensive web application designed to streamline the operations of a clothing store.

### Features

- **Users**:
  - View product listings
  - Filter products by category
  - Add products to the cart
  - Place orders

- **Managers**:
  - Manage products
  - Manage categories
  - Manage users through a robust admin panel

## Technologies

- **Backend**:
  - Python
  - Django Framework
  - DjangoORM
  - PostgreSQL
  - Redis
  - Celery
  - OAuth2.0

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/Vartan14/clothing-store.git
cd clothing-store
```

### Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Setup

- Create a PostgreSQL database.
- Update the database connection settings in `settings.py`.

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Open in your browser [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Access the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to manage products, categories, and users.
- Register a new user and log in to view and order products.
