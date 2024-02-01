# from rest_framework import serializers
# from .models import User, Book, BookDetails, BorrowedBooks

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'

# class BookDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookDetails
#         fields = '__all__'

# class BorrowedBooksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BorrowedBooks
#         fields = '__all__'
# library_app/serializers.py
from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'



class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = '__all__'
