import csv
from django.shortcuts import render
from django.contrib import messages
from django. contrib.auth.decorators import permission_required
from book.models import Book, Author, Category
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'index.html')

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    
    
    
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    num_category = Category.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_category': num_category,
        'num_visits': num_visits
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

    



#class BookListView(generic.ListView):
    #model = Book
    #paginate_by = 2

#class BookDetailView(generic.DetailView):
    #model = Book




    






