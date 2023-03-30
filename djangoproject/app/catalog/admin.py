from django.contrib import admin
from .models import Author, Language, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(BookInstance)