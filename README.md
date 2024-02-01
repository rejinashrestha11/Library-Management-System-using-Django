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
- MySQL
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

7. **Usage**
   ```bash
   python manage.py runserver
   
## API Endpoints

- **User Management:**
  - Create a new user: `/api/users/` (POST) - Mapped to `path('users/create/', UserCreateView.as_view(), name='user-create')`
  - List all users: `/api/users/` (GET) - Mapped to `path('users/', UserListView.as_view(), name='user-list')`
  - Get details of a specific user: `/api/users/<user_id>/` (GET) - Mapped to `path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail')`

- **Book Management:**
  - Add a new book: `/api/books/` (POST) - Mapped to `path('books/create/', BookCreateView.as_view(), name='book-create')`
  - List all books: `/api/books/` (GET) - Mapped to `path('books/', BookListView.as_view(), name='book-list')`
  - Get details of a specific book: `/api/books/<book_id>/` (GET) - Mapped to `path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail')`
  - Assign/update book details: `/api/books/<book_id>/details/` (POST) - Mapped to `path('books/<int:book_id>/add_details/', BookDetailsCreateView.as_view(), name='book-details-create')`

- **Book Details Management:**
  - Create book details for a specific book: `/api/books/<book_id>/details/` (POST) - Mapped to `path('books/<int:book_id>/add_details/', BookDetailsCreateView.as_view(), name='book-details-create')`
  - List book details for a specific book: `/api/books/<book_id>/details/` (GET) - Mapped to `path('books/<int:book_id>/list_details/', BookDetailsListView.as_view(), name='book-details-list')`

- **Borrowed Books Management:**
  - Borrow a book: `/api/borrowedbooks/` (POST) - Mapped to `path('borrowedbooks/create/', BorrowedBooksCreateView.as_view(), name='borrowedbooks-create')`
  - Return a book: `/api/borrowedbooks/<borrowed_book_id>/` (PUT) - Mapped to `path('borrowedbooks/<int:pk>/', BorrowedBooksDetailView.as_view(), name='borrowedbooks-detail')`
  - List all borrowed books: `/api/borrowedbooks/` (GET) - Mapped to `path('borrowedbooks/', BorrowedBooksListView.as_view(), name='borrowedbooks-list')`

## Testing

Run the tests:

```bash
python manage.py test
