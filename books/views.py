from django.http import JsonResponse
from django.core.cache import cache
import requests

def get_book_name(request):
    isbn = request.GET.get('isbn')

    cached_book_name = cache.get(isbn)
    if cached_book_name:
        return JsonResponse({'book_name': cached_book_name})
        
    # Fetch book name from external service (Open Library API)
    response = requests.get(f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data')
    book_data = response.json()

    # Extract book name from the response
    book_name = book_data.get(f'ISBN:{isbn}', {}).get('title', 'Book not found')
    cache.set(isbn, book_name, timeout=3600)
    

    return JsonResponse({'book_name': book_name[::-1]})
