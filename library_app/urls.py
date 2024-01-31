# library_app/urls.py
from django.urls import path
from .views import (
    UserListView, UserCreateView, UserDetailView,
    BookListView, BookCreateView, BookDetailView,
    BorrowedBooksListView, BorrowedBooksCreateView, BorrowedBooksDetailView
)

urlpatterns = [
    # User URLs
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # BorrowedBooks URLs
    path('borrowedbooks/', BorrowedBooksListView.as_view(), name='borrowedbooks-list'),
    path('borrowedbooks/create/', BorrowedBooksCreateView.as_view(), name='borrowedbooks-create'),
    path('borrowedbooks/<int:pk>/', BorrowedBooksDetailView.as_view(), name='borrowedbooks-detail'),
]
