# Baby Tools Shop – Django Server Project

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
 - Docker
 - Docker compose
 - Python 3.9

### 1. Clone the repository
```bash
git clone https://github.com/tnkprbxyg-maker/baby-tools-shop.git
cd baby-tools-shop
```

### 2. Create environment file
```bash
cp  example.env
```


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
(http://<your_ip>:8000)

 ## Usage

This section explains how to build, run, stop, and configure the application using Docker.

### 1. Build the Docker image
From the project root directory, run:

```bash
docker build -t baby-tools-shop .

**2.⁠ ⁠Run the application**

Start the container and expose the application on port 8000:
docker run --rm -p 8000:8000 baby-tools-shop

**Open the application in your browser:**
	•	http://localhost:8000
	•	Django Admin: http://localhost:8000/admin

**3.⁠ ⁠Stop the application**

To stop the running container, press:
Ctrl+C

**4.⁠ ⁠Run the container in background (optional)**

You can also run the container in detached mode:
docker run -d --name baby-tools-shop --rm -p 8000:8000 baby-tools-shop

To stop it later, run:
docker stop baby-tools-shop

**5.⁠ ⁠Use a different port (optional)**

If port 8000 is already in use, you can bind a different host port (for example 8025):
docker run --rm -p 8025:8000 baby-tools-shop

Then open:
	•	http://localhost:8025

**6.⁠ ⁠Create a Django superuser**

To access the Django admin interface, create a superuser inside the running container:
docker ps
docker exec -it <container_id> python manage.py createsuperuser

Follow the prompts to set username, email, and password.

**7.⁠ ⁠Django Admin Interface**

Open the admin panel in your browser:
	•	http://localhost:8000/admin

Log in using the superuser credentials to manage products and categories.


