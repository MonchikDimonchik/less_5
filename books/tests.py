# Create your tests here.
from django.urls import reverse
from django.test import TestCase
from .models import Book
from .factories import BookFactory

class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем 10 книг
        for _ in range(10):
            BookFactory()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_pagination_is_ten(self):
        # Создаем больше книг, чем нужно для одной страницы (больше 10)
        BookFactory.create_batch(15)

        response = self.client.get(reverse('book_list'))

        # Проверяем, что пагинация включена
        self.assertTrue(response.context['is_paginated'])

        # Проверяем, что на странице находится ровно 10 книг
        self.assertEqual(len(response.context['books']), 10)

    def test_lists_all_books(self):
        Book.objects.all().delete()  # Удаляем все книги перед тестом
        BookFactory.create_batch(10)  # Создаем ровно 10 книг
        response = self.client.get(reverse('book_list'))
        self.assertEqual(len(response.context['books']), 10)


def test_create_book(self):
    book_data = {
        'title': 'New Book',
        'author': 'Author Name',
        'published_date': '2022-01-01',
        'isbn_number': '1234567890123',
        'pages': 200,
        'language': 'EN',
        'description': 'Test Description',
        'price': '19.99'  # Добавляем поле цены
    }
    response = self.client.post(reverse('book_create'), data=book_data)
    self.assertEqual(response.status_code, 302)  # Ожидается редирект
    self.assertTrue(Book.objects.filter(title='New Book').exists())

class BookUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = BookFactory(title='Original Title')

    def test_update_book(self):
        response = self.client.post(reverse('book_edit', args=[self.book.id]), {
            'title': 'Updated Title',
            'author': 'Updated Author',
            'published_date': '2022-01-01',
            'isbn_number': '1234567890123',
            'pages': 300,
            'language': 'EN',
            'description': 'Updated description',
        })
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

class BookDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = BookFactory()

    def test_delete_book(self):
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())