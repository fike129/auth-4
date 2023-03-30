import uuid

from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=255, help_text='Enter Author name')
    date_of_birth = models.DateField(null=True, blank=True)
    dte_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text="Enter genre")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100, help_text="Enter language")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Enter book title")
    author = models.ManyToManyField(Author, null=True)
    summary = models.CharField(max_length=1000, help_text="Enter book description")
    genre = models.ManyToManyField(Genre, null=True)
    language = models.ForeignKey(Language, models.SET_NULL, null=True)
    ISBN = models.CharField('ISBN', max_length=13,
                            help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    book = models.ForeignKey(Book, models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.book.title} {self.id}'
