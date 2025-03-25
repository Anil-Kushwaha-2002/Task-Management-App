# Task Management App
API Development in Django/Python

# Task Management API

## 📌 Project Overview

The Task Management API is a RESTful web service built with Django and Django Rest Framework (DRF) to manage tasks efficiently. It allows users to create, assign, and track tasks while supporting multiple user assignments per task.

## 🚀 Features

- User Authentication (Custom User Model with JWT)

- Task Management (Create, Retrieve, Update, Delete)

- Task Assignment (Assign multiple users to a task)

- Status Tracking (Pending, In Progress, Completed)

- Pagination & Filtering for better task organization

- Role-Based Access Control using DRF Permissions


## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts to set credentials
```
### 5. Run the Development Server
```bash
python manage.py runserver
```
The API will be available at http://127.0.0.1:8000/


# 🔗 API Endpoints

## User Authentication - Register a admin

POST /admin/

### Request Body:
```bash
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword"
}
```
### Response:
```bash
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
}
```
## Login & Get Token

POST /users/

### Response:
```bash
{
    "access": "your_jwt_token_here",
    "refresh": "your_refresh_token_here"
}
```
# Task Management

## Create a Task

POST /tasks/

### Request Body:
```bash
{
    "name": "Project Meeting",
    "description": "Discuss project timeline",
    "status": "pending"
}
```
### Response:
```bash
{
    "id": 1,
    "name": "Project Meeting",
    "description": "Discuss project timeline",
    "status": "pending",
    "assigned_users": []
}
```
## Assign Users to a Task

PATCH /tasks/1/assign/

### Request Body:
```bash
{
    "assigned_users": [1, 2]
}
```
### Response:
```bash
{
    "id": 1,
    "assigned_users": [1, 2]
}
```
### Retrieve Tasks for a User
