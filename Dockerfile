# Python image
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create and set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Make entrypoint executable
RUN chmod +x scripts/entrypoint.sh

# Entrypoint
ENTRYPOINT ["/app/scripts/entrypoint.sh"]

# Yangi foydalanuvchi yaratish va huquqlarni sozlash
RUN useradd -m myuser && \
    chown -R myuser:myuser /app

WORKDIR /app
USER myuser

# Keyingi buyruqlar (masalan, CMD)
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]



