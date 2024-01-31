# library_app/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Book, BorrowedBooks

class LibraryAppAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create some test data
        self.user = User.objects.create(Name='John Doe', Email='john@example.com', MembershipDate='2022-01-01')
        self.book = Book.objects.create(Title='Sample Book', ISBN='1234567890123', PublishedDate='2022-01-01', Genre='Fiction')
        self.borrowed_book = BorrowedBooks.objects.create(UserID=self.user, BookID=self.book, BorrowDate='2022-01-01')

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrowedbooks_list(self):
        url = reverse('borrowedbooks-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed for other views
