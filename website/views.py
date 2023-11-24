from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author, Book
from .forms import AddBookForm, EditBookForm
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def list_books(request):
    authors = Author.objects.all()
    books = Book.objects.filter(in_stock=True)
    #books = Book.objects.all()

    return render(request, 'list_books.html', {'books': books, 'authors': authors})

def list_all_books(request):
    authors = Author.objects.all()
    books = Book.objects.all()

    return render(request, 'list_books.html', {'books': books, 'authors': authors})

def add_book(request):
    form = AddBookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            adding_book = form.save()
            messages.success(request, "Book added successfully")
            return redirect('list_book')

    return render(request, 'add_book.html', {'form':form})

def one_book(request, pk):
    one_book = Book.objects.get(id = pk)
    return render(request, 'book.html', {'one_book':one_book})

def edit_book(request, pk):
    edited_book = Book.objects.get(id = pk)
    form = EditBookForm(request.POST or None, instance=edited_book)

    if form.is_valid():
        form.save()
        messages.success(request, "Book has been updated!")
        return redirect('list_book')

    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, pk):
    deleted_book = Book.objects.get(id = pk)
    deleted_book.delete()
    messages.success(request, "Book has been deleted!")
    return redirect('list_book')

def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(Q(title__contains = searched) | Q(author__name__contains = searched))
        return render(request, 'search_book.html', {'searched':searched, 'books': books})
    else:
        return render(request, 'search_book.html', {})