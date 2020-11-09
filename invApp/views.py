from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "allTheBooks": Book.objects.all(),
        "allTheAuthors": Author.objects.all()
    }
    return render(request, "index.html", context)

def addBook(request):
    Book.objects.create(title=request.POST["title"],desc=request.POST["desc"])
    return redirect('/')

def authorPage(request):
    context = {
        "allTheBooks": Book.objects.all(),
        "allTheAuthors": Author.objects.all()
    }
    return render(request,"authorPage.html",context)

def addAuthor(request):
    Author.objects.create(firstName=request.POST["firstName"],lastName=request.POST["lastName"],notes=request.POST["notes"])
    return redirect('/authorPage')

def singleBook(request,myVal):
    context = {
        "oneBook": Book.objects.get(id=int(myVal)),
        "allTheAuthors": Author.objects.all()
    }
    return render(request,"singleBook.html",context)

def appendAuthor(request,bookId):
    author = Author.objects.get(id=request.POST['author'])
    book = Book.objects.get(id=request.POST['book'])
    book.publishers.add(author)
    url = (f"/singleBook/{bookId}")
    return redirect(url)

def singleAuthor(request,myVal):
    context = {
        "oneAuthor": Author.objects.get(id=int(myVal)),
        "allTheBooks": Book.objects.all()
    }
    return render(request,"singleAuthor.html",context)


def appendBook(request,authorId):
    author = Author.objects.get(id=request.POST['author'])
    book = Book.objects.get(id=request.POST['book'])
    author.books.add(book)
    url = (f"/singleAuthor/{authorId}")
    return redirect(url)
