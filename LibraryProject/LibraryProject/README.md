# LibraryProject

## Introduction
This project is part of the **Introduction to Django Development Environment Setup** task.  
The goal is to gain familiarity with Django by setting up a Django development environment and creating a basic Django project.  


## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate   # For Git Bash on Windows

## 2. Install Django
pip install django

## 3. Verify Installation
python -m django --version

## 4. Create Django Project
django-admin startproject LibraryProject

## 5. Navigate into the Project
cd LibraryProject

## 6. Run the Development Server
python manage.py runserver

Then visit http://127.0.0.1:8000/
 in your browser to see the default Django welcome page.

The Project Structure
 LibraryProject/
│
├── manage.py                # Command-line utility for Django project
├── LibraryProject/          # Main project folder containing configuration files
│   ├── __init__.py
│   ├── settings.py          # Project settings/configuration
│   ├── urls.py              # URL declarations for the project
│   ├── asgi.py
│   └── wsgi.py
└── README.md                # Project documentation

manage.py → Used to run server, migrations, and other commands.

settings.py → Stores all project settings (database, installed apps, etc.).

urls.py → Maps URLs to views (the website’s “table of contents”).

asgi.py / wsgi.py → Help run Django with web servers.

