from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BooksManager(models.Manager):
    def add(self, title, author, category):
        messages = []

        if len(title) < 1:
            messages.append('Title cannot be blank.')
        if len(author) < 1:
            messages.append('Author cannot be blank.')
        if len(category) < 1:
            messages.append('Category cannot be blank.')
        
        if len(messages) > 0:
            return False, messages
        else:
            book = Books.booksManager.create(title=title, author=author, category=category)
            return (True, Books)


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    booksManager = BooksManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

