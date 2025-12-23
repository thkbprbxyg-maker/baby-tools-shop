<<<<<<< HEAD
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

- **Python 3.10.13**
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
=======
# Baby Tools Shop – Django Demo Project


Baby Tools Shop is a simple e-commerce demo application built with Django.  
The project is intended as a learning and demonstration project and includes user authentication, product and category management, and an admin interface.  
It is containerized with Docker to allow an easy and reproducible setup.

---


 ## Table of Contents
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Further Information](#further-information)

 ## Quickstart
 Follow these steps to run the project locally using Docker:

### 1. Clone the repository
```bash
git clone https://github.com/tnkprbxyg-maker/baby-tools-shop.git
cd baby-tools-shop
```

2. Change into the project directory: cd baby-tools-shop
3. Create a .env file based on the example: cp example.env .env
### 2. Create environment file
```bash
cp example.env .env
```

4. Build the Docker image: docker build -t baby-tools-shop .
5. Run the container: docker run -p 8000:8000 baby-tools-shop
### 3. Build Docker image
```bash
docker build -t baby-tools-shop .
```

6. Open the application in your browser: http://localhost:8000
### 4. Run the container
```bash
docker run -p 8000:8000 baby-tools-shop
```

### 5. Open the application
Open your browser and navigate to:  
http://localhost:8000

 ## Usage

### Create a Django superuser

To access the Django admin interface, create a superuser inside the running container:

```bash
docker ps
docker exec -it <container_id> python manage.py createsuperuser
```

Follow the prompts to set username, email and password.

### Django Admin Interface

Open the admin panel in your browser:  
http://localhost:8000/admin

Log in using the superuser credentials to manage products and categories.

 ## Further Information
 This project uses Django with SQLite for demonstration purposes.