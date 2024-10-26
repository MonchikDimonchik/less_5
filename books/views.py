from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.views.generic import TemplateView
from django_filters.views import FilterView
from .filters import BookFilter
from rest_framework import viewsets
from .serializers import BookSerializer
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from books import filters


# Представление для главной страницы
class HomePageView(TemplateView):
    template_name = 'home.html'


# Представление списка книг
class BookListView(FilterView):
    model = Book
    filterset_class = BookFilter
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10


# Представление деталей книги
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


# Представление для создания книги
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn_number', 'pages', 'language', 'description']


# Представление для обновления книги
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'published_date', 'isbn_number', 'pages', 'language', 'description']


# Представление для удаления книги
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer