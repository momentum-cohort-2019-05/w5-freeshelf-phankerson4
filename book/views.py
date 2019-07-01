import csv
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django. contrib.auth.decorators import login_required
from django.http import HttpResponse
from book.models import Book, Category, UserFavs
from django.views import View
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

class BookListView(View):
     def get(self, request):
        form = BookForm()
        return self.render_template(request, form)


    #def post(self, request):
        #if request.user.is_authenticated:
            #form= BookForm(data=request.POST)
            #if form.is_valid():
            #book = form.save(commit=False)
            #book.owner = request.user
            #book.save()
            #messages.success(
            #request,
            #f"Your book '{book.name}' was created successfully."
            #)
        #return redirect(to='book-list')
        #else:
            #form = BookForm()
        #return self.render_template(request, form)
        

    

def render_template(self, request, form):
        if request.user.is_authenticated:
            my_books = Book.objects.filter(owner=request.user)
            other_books = Book.objects.exclude(owner=request.user)
        else:
            my_books = []
            other_books = Book.objects.all()

        return render(request, 'book/book_list.html', {
            "my_books": my_books,
            "other_books": other_books,
            "form": form
        })

#class BookDetailView(DetailView):
    #model = Book
    # Render the HTML template index.html with the data in the context variable
    #return render(request, 'index.html', context=context)

    





#class BookDetailView(generic.DetailView):
    #model = Book




    






