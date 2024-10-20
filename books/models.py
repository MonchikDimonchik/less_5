from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    published_date = models.DateField(verbose_name="Дата публикации")
    isbn_number = models.CharField(max_length=13, verbose_name="ISBN")
    pages = models.IntegerField(verbose_name="Страницы")
    language = models.CharField(max_length=10, verbose_name="Язык")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")  # Добавляем поле для цены
    storage_amount = models.IntegerField(default=0, verbose_name="Количество на складе")  # Новое поле для количества книг на складе


    def __str__(self):
        return self.title

    @property
    def is_in_stock(self):
        return self.storage_amount > 0

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
