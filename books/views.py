from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from django.views.generic import TemplateView


# Представление для главной страницы
class HomePageView(TemplateView):
    template_name = 'home.html'


# Представление списка книг
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'


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