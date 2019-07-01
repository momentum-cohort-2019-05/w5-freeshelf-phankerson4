from django import forms
from core.models import Book, Category


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name',)


class CatgoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = (
            'name',
            
        )


#class BookResultsForm(forms.Form):
    #correct = forms.BooleanField(required=False)
