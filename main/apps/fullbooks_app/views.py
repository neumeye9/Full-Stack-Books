from django.shortcuts import render, redirect
from models import Books


# Create your views here.

def index(request):
    books = Books.booksManager.all()
    context = {
        "books": books
    }
    return render(request, 'fullbooks_app/index.html', context)

def addbook(request):

    check = Books.booksManager.add(request.POST['title'], request.POST['author'], request.POST['category'])

    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)

    print check 
    return redirect('/')