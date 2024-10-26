from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from books.views import HomePageView  # Импортируем представление главной страницы

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # Подключаем маршруты для книг
    path('', HomePageView.as_view(), name='home'),  # Главная страница
    path('api/', include('books.urls')),  # Маршруты для API
    path('api/', include('books.urls')),    # Подключение API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),                   # JSON-схема OpenAPI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]
