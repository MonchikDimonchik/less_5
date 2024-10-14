from django.contrib import admin
from django.urls import path, include
from books.views import HomePageView  # Импортируем представление главной страницы

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # Подключаем маршруты для книг
    path('', HomePageView.as_view(), name='home'),  # Главная страница
]
