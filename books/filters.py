import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Автор')
    published_date = django_filters.DateFilter(label='Дата публикации')
    price = django_filters.RangeFilter(label='Цена (от-до)')  # Фильтр по диапазону цены
    available = django_filters.BooleanFilter(method='filter_available', label='В наличии')

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'price']

    # Метод для фильтрации по наличию книг
    def filter_available(self, queryset, name, value):
        if value:
            return queryset.filter(storage_amount__gt=0)
        return queryset.filter(storage_amount=0)