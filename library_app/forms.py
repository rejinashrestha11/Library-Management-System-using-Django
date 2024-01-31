# library_app/forms.py
from django import forms
from .models import User, Book, BookDetails, BorrowedBooks

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'Email', 'MembershipDate']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['Title', 'ISBN', 'PublishedDate', 'Genre']

class BookDetailsForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = ['NumberOfPages', 'Publisher', 'Language']

class BorrowedBooksForm(forms.ModelForm):
    class Meta:
        model = BorrowedBooks
        fields = ['BorrowDate', 'ReturnDate']
