from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListAPIView, RetrieveAPIView


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "slug"