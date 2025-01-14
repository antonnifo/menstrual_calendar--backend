# Menstrual Calendar API

This is a **Django REST Framework (DRF)** project for managing user data and menstrual cycles. It provides a backend API to handle CRUD operations on **users** and their **menstrual cycles**.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **User Management**: CRUD operations for managing user accounts.
- **Cycle Management**: CRUD operations for managing menstrual cycle data.
- **RESTful API**: Built using Django REST Framework for easy interaction.

---

## Project Structure

```
menstrual_calendar/
│
├── cycles/             # App for managing cycles
│   ├── models.py       # Database models for cycles
│   ├── views.py        # API views for cycle CRUD operations
│   ├── serializers.py  # Serializers for handling JSON data
│   └── urls.py         # Routes for cycle endpoints
│
├── users/              # App for managing users
│   ├── models.py       # Database models for users
│   ├── views.py        # API views for user CRUD operations
│   ├── serializers.py  # Serializers for handling user data
│   └── urls.py         # Routes for user endpoints
│
├── requirements.txt    # Project dependencies
├── manage.py           # Django project manager
└── menstrual_calendar/ # Project configuration (settings, URLs, WSGI)
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## Requirements

Ensure you have the following installed:

- **Python 3.8+**
- **Django 4.x**
- **Django REST Framework**

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd menstrual_calendar
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

---

## Running the Project

Start the development server:

```bash
python manage.py runserver
```

Access the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue.

---

