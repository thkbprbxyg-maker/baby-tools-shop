FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY babyshop_app /app/babyshop_app

WORKDIR /app/babyshop_app

EXPOSE 8025

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8025"]
