# Baby Tools Shop – Django Server Project

A simple online shop for baby products, built with **Django** and deployed on a **Linux VPS**.  
This project was created as part of a **server & deployment module** to demonstrate backend development, server setup, and public deployment.

---

## Live Demo



---

## Features

- User registration & login
- Product and category management
- Admin dashboard (Django Admin)
- Product overview with images
- Server-side database
- Public access via VPS & IP address

---

## Tech Stack

- **Python 3.12**
- **Django 4.0.2**
- **SQLite** (server-side, demo purposes)
- **Linux VPS (Hetzner)**
- **UFW Firewall**
- **SSH deployment**

---

## Server & Deployment

- The application is deployed on a **Virtual Private Server (VPS)**.
- The Django development server runs on **port 8000**.
- Firewall rules allow external access to the application.
- Products and categories are managed via the Django admin interface.
- The database is hosted on the server and independent from the local environment.

---

## Run Locally

```bash
git clone https://github.com/thkbprbxyg-maker/baby-tools-shop.git
cd baby-tools-shop
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
