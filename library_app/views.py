# library_app/views.py
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        return get_object_or_404(Book, pk=self.kwargs['pk'])

class BookDetailsCreateView(generics.CreateAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer

class BookDetailsListView(generics.ListAPIView):
    serializer_class = BookDetailsSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return BookDetails.objects.filter(Book=book_id)

class BorrowedBooksListView(generics.ListAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

class BorrowedBooksCreateView(generics.CreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

class BorrowedBooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

    def get_object(self):
        return get_object_or_404(BorrowedBooks, pk=self.kwargs['pk'])
