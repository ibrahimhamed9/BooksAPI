from django.contrib import admin
from django.urls import path
from books.views import get_book_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book-name/', get_book_name, name='get_book_name'),
]
