from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
# ------------------------------------------------------------------------|
# initial method

def index(request):
    return render(request, 'books.html', {"books": Book.objects.all()})

def authors(request):
    return render(request, 'authors.html', {"authors": Author.objects.all()})

def create_book(request):
    Book.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect('/books')

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request,'book.html', context)

def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors__id=author_id)
    }
    return render(request, 'author.html', context)

def create_author(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')

def assign_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')

def assign_author(request, author_id):
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f'/authors/{author_id}')