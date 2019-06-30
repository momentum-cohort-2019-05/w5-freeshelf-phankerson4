from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('category-detail', args=[str(self.id)])


    

    class Meta:
        ordering = ["name"]
        verbose_name = "Categorie"

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=1000, help_text='Description of the book')
    #isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    category= models.ManyToManyField(Category)
    
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    name = models.CharField(max_length=100, default='anonymous')
    def __str__(self):
        return self.name

class UserFavs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'fav_book']
        ordering = ['-date_added']

    def __str__(self):
        return self.fav_book.title
