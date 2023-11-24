from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('list_books/', views.list_books, name = 'list_book'),
    path('list_all_books/', views.list_all_books, name = 'list_all_book'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('book/<int:pk>', views.one_book, name = 'one_book'),
    path('edit_book/<int:pk>', views.edit_book, name = 'edit_book'),
    path('delete_book/<int:pk>', views.delete_book, name = 'delete_book'),
    path('search', views.search_book, name = 'search_book'),
]