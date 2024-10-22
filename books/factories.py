import factory
from factory.django import DjangoModelFactory
from .models import Book

class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')
    published_date = factory.Faker('date_object')
    isbn_number = factory.Faker('isbn13')
    pages = factory.Faker('random_int', min=100, max=500)
    language = factory.Faker('language_code')
    description = factory.Faker('text', max_nb_chars=200)
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    storage_amount = factory.Faker('random_int', min=0, max=100)