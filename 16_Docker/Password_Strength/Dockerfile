# Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files into the container
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run your app
CMD ["python", "password_strength.py"]
