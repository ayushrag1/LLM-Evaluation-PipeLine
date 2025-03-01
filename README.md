This file contains the step to run a **LLM Evaluation Pipeline**  Django application using Docker and Docker Compose. It includes installation steps, environment setup, database migration, and how to access the app.

---
# LLM Evaluation Pipeline

This repository contains an **LLM Evaluation Pipeline** that integrates the following technologies:
- **Celery**
- **Redis**
- **Django**
- **Django Rest Framework**

The project implements an **LLM Evaluator** application that can be easily set up and run using **Docker** and **Docker Compose**.

## Features
- Scalable evaluation pipeline using Celery and Redis.
- Easy deployment with Docker and Docker Compose.
- RESTful API built with Django Rest Framework.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Python 3.10.12](https://www.python.org/downloads/) (if running locally without Docker)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/ayushrag1/LLM-Evaluation-PipeLine.git
cd LLM Evaluation PipeLine
```

### 2️⃣ Create a `.env` File (Optional)

If your project uses environment variables, create a `.env` file:

```sh
touch .env
```

Add variables (example):

```env
# Django app Related Config
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key

# Redis Configuration (Use the service name `redis` instead of localhost)
REDIS_URL=redis://redis:6379/0

# Email Configuration (No extra spaces or quotes)
EMAIL_HOST_USER=sender-email-id
EMAIL_HOST_PASSWORD=email-app-password

# Postgres Database Configuration
POSTGRES_DB=llm_evaluator
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

```

---

## 🐳 Running with Docker

### 1️⃣ Build and Run Containers

```sh
docker compose up -d --build
```

> `-d`: Runs in detached mode (background).
> `--build`: Rebuilds the images if there are changes.

### 2️⃣ Create a Superuser (Admin Access)

```sh
docker compose exec web python manage.py createsuperuser
```

Follow the prompts to set up an admin user.

---

## 🏃 Running Locally Without Docker

If you prefer to run the app without Docker:

### 1️⃣ Create and Activate Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 3️⃣ Run Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Start the Django Development Server

```sh
python manage.py runserver
```

---

## 📜 Useful Docker Commands

- View logs:
  ```sh
  docker compose logs -f
  ```

- Stop Containers:
  ```sh
  docker compose down
  ```

- Restart Containers:
  ```sh
  docker compose restart
  ```

- View all Docker Volumes:
  ```sh
  docker volume ls
  ```

- Delete Docker Volume:
  ```sh
  docker volume rm <volume_name>
  ```

---

## 🔗 Access the Application

- **App URL**: [http://localhost:8000](http://localhost:8000)
- **Admin Panel**: [http://localhost:8000/admin](http://localhost:8000)

Login using the superuser credentials you created.


## 🎯 Troubleshooting

- **Check running containers**
  ```sh
  docker ps
  ```

- **Check container logs**
  ```sh
  docker compose logs -f web
  ```

- **Enter the container shell**
  ```sh
  docker compose exec web sh
  ```

---

## ✨ Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ❤️ Support

If you find this project helpful, consider giving it a ⭐ on GitHub! 🚀

---

This README covers **everything** from setup to troubleshooting. Let me know if you need modifications! 🚀
