# Use official Python image
FROM python:3.10.12

# Install PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Environment variables to prevent .pyc files and buffer issues
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Copy dependencies first to leverage Docker caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY . .

# Ensure the script is executable
RUN chmod +x run_app.sh

# Default command to run the app (can be overridden by docker-compose)
CMD ["bash", "run_app.sh"]
