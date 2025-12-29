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

### 1. Clone the repository
```bash
git clone https://github.com/tnkprbxyg-maker/baby-tools-shop.git
cd baby-tools-shop
```

2. Change into the project directory: cd baby-tools-shop
3. Create a .env file based on the example: cp example.env .env
### 2. Create environment file
```bash
cp  .env
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
