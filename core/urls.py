from django.urls import path
from .views import BookListView, BookDetailView


urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path("books/<slug:slug>/", BookDetailView.as_view(), name="book-detail"),
]