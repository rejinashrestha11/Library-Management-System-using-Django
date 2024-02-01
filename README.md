# Django Library Management System

A Django-based library management system with APIs for managing users, books, book details, and borrowed books.

## Features

- **User Management:**
  - Create a new user
  - List all users
  - Get details of a specific user

- **Book Management:**
  - Add a new book
  - List all books
  - Get details of a specific book
  - Assign/update book details

- **Book Details Management:**
  - Create book details for a specific book
  - List book details for a specific book

- **Borrowed Books Management:**
  - Borrow a book
  - Return a book
  - List all borrowed books

## Prerequisites

- Python 3.6+
- Django 3.0+
- MySQL or another database
- Other dependencies (see `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone system https://github.com/rejinashrestha11/Library-Management-System-using-Django

2. **Navigate to the project directory:**

   ```bash
   cd library-management-system
   
3. **Set up a virtual environment:**

   ```bash
   python -m venv lib
   
4. **Activate a virtual environment:**
 - **On Windows:**
   ```bash
   lib\scripts\activate
   
 - **On MacOS/Linux:**
   ```bash
   source lib/bin/activate

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
6. **Run Migrations**
   ```bash
   python manage.py migrate
