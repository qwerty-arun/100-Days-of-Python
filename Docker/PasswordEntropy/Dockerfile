# 1. Start with a base image
FROM python:3.9-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy files from host machine to container
COPY app.py .

# 4. Define what happens when the container runs
CMD ["python", "app.py"]