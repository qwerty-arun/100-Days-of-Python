# Base image with Python
FROM python:3.11-slim

# Set Working Directory
WORKDIR /app

# Copy Files into the container
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run your app
CMD ["python", "intro_script_gen.py"]