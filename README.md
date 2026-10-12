# Little Lemon — Restaurant Website

A Django-powered restaurant website featuring a database-driven menu, individual dish pages, image management, a customized administration interface, and responsive styling.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-07405E?style=flat&logo=sqlite&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS-E34F26?style=flat&logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-blue?style=flat)
![License](https://img.shields.io/badge/License-Not%20specified-lightgrey?style=flat)

## Overview

Little Lemon is a restaurant website built with Django, demonstrating how a server-rendered web application can manage and display content stored in a relational database.

Instead of hardcoding menu items into HTML, the application uses Django models and the ORM to retrieve dish information dynamically. The built-in Django administration interface allows authorized staff to manage menu content without directly modifying application code.

The project demonstrates core Django development practices, including the Model-View-Template (MVT) architecture, reusable templates, class-based views, media handling, and database migrations.

## Features

### Dynamic Menu

- Display menu items retrieved from the database.
- Sort menu items alphabetically.
- Show dish information, including names, descriptions, prices, and images.
- Provide individual detail pages for menu items.

### Image Management

- Store dish images using Django's `ImageField`.
- Process uploaded images with Pillow.
- Display uploaded media in menu listings and detail pages.

### Administration Dashboard

- Manage menu items through Django Admin.
- Customize the displayed columns and search behavior.
- Add, edit, and delete menu entries without changing application code.

### Restaurant Information

- Homepage introducing the restaurant.
- About page with restaurant information.
- Reservation page displaying contact information.

The reservation page is informational; a complete reservation booking workflow is not currently implemented.

### Responsive Interface

- Custom CSS styling without a heavy frontend framework.
- Reusable page layouts with Django template inheritance.
- Shared navigation, content sections, and footer elements.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend language |
| Django 5.x | Web framework |
| Django ORM | Database access and model management |
| SQLite | Development database |
| Django Template Language | Server-side HTML rendering |
| Django Admin | Menu administration |
| HTML5 | Page structure |
| CSS3 | Responsive styling |
| Pillow | Image processing and image uploads |

## Architecture

The application follows Django's Model-View-Template architecture.

```text id="f82t2k"
Browser
   |
   v
URL Routing
   |
   v
Django Views
   |
   +-------------------+
   |                   |
   v                   v
Django Models      Templates
   |
   v
Django ORM
   |
   v
SQLite Database

Django Admin
   |
   v
Menu Management
```

### Main Components

- **Models:** Define menu items and their stored attributes.
- **Views:** Retrieve menu data and prepare responses.
- **Templates:** Render the homepage, menu listing, and dish details.
- **Admin:** Provides an administration interface for authorized users.
- **Static files:** Store custom CSS and other frontend assets.
- **Media files:** Store uploaded dish images during development.

## Project Structure

```text id="q29g8v"
Restaurant-django/
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── restaurant/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│   └── migrations/
├── Templates/
│   └── restaurant/
├── static/
├── media/
│   └── menu_images/
└── manage.py
```

## Getting Started

### Prerequisites

- Python 3.10 or later, compatible with the installed Django version.
- pip
- A terminal or IDE

### 1. Clone the Repository

```bash id="2ujl2u"
git clone https://github.com/ELGHAD/Restaurant-django.git
cd Restaurant-django
```

### 2. Create a Virtual Environment

```bash id="h9ed92"
python -m venv venv
```

Activate it on Linux or macOS:

```bash id="h9ed93"
source venv/bin/activate
```

On Windows:

```powershell id="h9ed94"
venv\Scripts\activate
```

### 3. Install Dependencies

If the repository does not include a `requirements.txt` file, install the required packages manually:

```bash id="h9ed95"
python -m pip install "Django>=5.0,<6.0" Pillow
```

For a reproducible setup, pin the versions that have been tested with the project and save them in a `requirements.txt` file.

### 4. Apply Database Migrations

```bash id="h9ed96"
python manage.py migrate
```

### 5. Create an Administrator Account

```bash id="h9ed97"
python manage.py createsuperuser
```

Follow the prompts to configure the administrator credentials.

### 6. Run the Development Server

```bash id="h9ed98"
python manage.py runserver
```

Open the application at:

- Website: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin dashboard: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Uploaded images and their display depend on the project's media configuration. Django's development server is intended for local development, not production hosting.

## Security and Development Practices

The project uses several standard Django mechanisms:

- **ORM-based queries:** Use Django's ORM for database access rather than manually constructing SQL queries.
- **CSRF protection:** Django's standard CSRF middleware protects applicable form submissions.
- **Admin access control:** Django Admin restricts access to appropriately authorized staff users.
- **Class-based views:** `ListView` and `DetailView` reduce repetitive code for listing and displaying menu items.
- **Template inheritance:** Shared layouts help maintain consistent page structure.
- **Database migrations:** Track and apply database schema changes.

### Production Considerations

The current development configuration needs to be hardened before deployment:

- Move `SECRET_KEY` into an environment variable and ensure it is not exposed in source control.
- Set `DEBUG = False` in production.
- Configure `ALLOWED_HOSTS` for the intended deployment domain.
- Configure static and uploaded media file serving appropriately.
- Review file upload validation, size limits, and storage permissions.
- Consider PostgreSQL for a production deployment requiring more robust database operations.

## Current Limitations

This project is a restaurant website demonstration rather than a complete restaurant management platform.

- The reservation page is informational and does not implement a full booking workflow.
- No customer authentication or reservation history is documented.
- Automated tests need to be added for menu views and application behavior.
- A dependency lock or pinned requirements file should be added for reproducible installation.
- Production deployment and media storage require additional configuration.

## Potential Improvements

1. Implement a reservation form with availability validation and booking persistence.
2. Add automated tests for models, views, routes, and admin behavior.
3. Add search and category filtering to the menu.
4. Introduce Django REST Framework to expose a menu API.
5. Move configuration to environment variables.
6. Add deployment documentation and a production-ready static/media strategy.
7. Configure continuous integration to run tests automatically.

## Author

**Hamza Elrhadiouini**

- GitHub: [@ELGHAD](https://github.com/ELGHAD)
- Portfolio: [elghad.github.io/hamza-elrhadiouini-portfolio](https://elghad.github.io/hamza-elrhadiouini-portfolio)
