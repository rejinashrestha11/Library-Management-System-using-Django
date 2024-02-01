# library_app/urls.py
from django.urls import path
from .views import (
    UserListView, UserCreateView, UserDetailView,
    BookListView, BookCreateView, BookDetailView, BookDetailsCreateView, BookDetailsListView,
    BorrowedBooksListView, BorrowedBooksCreateView, BorrowedBooksDetailView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:book_id>/list_details/', BookDetailsListView.as_view(), name='book-details-list'),
    path('books/<int:pk>/add_details/', BookDetailsCreateView.as_view(), name='book-details-create'),

    path('borrowedbooks/', BorrowedBooksListView.as_view(), name='borrowedbooks-list'),
    path('borrowedbooks/create/', BorrowedBooksCreateView.as_view(), name='borrowedbooks-create'),
    path('borrowedbooks/<int:pk>/', BorrowedBooksDetailView.as_view(), name='borrowedbooks-detail'),
]
