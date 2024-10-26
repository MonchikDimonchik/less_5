from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# Создаем роутер и регистрируем представление BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('', include(router.urls)),

]
