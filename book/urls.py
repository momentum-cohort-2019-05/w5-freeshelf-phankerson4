

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from book import views as book_views

from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    #path('books/', views.BookListView.as_view(), name='books'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),  
    #path('accounts/', include('registration.backends.simple.urls')),
    
]






#if settings.DEBUG:
    #import debug_toolbar
    #urlpatterns = [
        #path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    #] + urlpatterns
