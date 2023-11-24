from django import forms
from .models import Book

class DateInput(forms.DateInput):
    input_type = 'date'

# Add book form
class AddBookForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Title of the book", "class":"form-control"}), label= "", max_length=150)
    #published_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'Published date (YYYY-MM-DD)', "class":"form-control"}), label= "", input_formats=['%Y-%m-%d'])
    published_date = forms.DateField(required=True, widget=forms.DateInput(format = ('%d/%m/%Y'), attrs={'placeholder': 'Published date (DD-MM-YYYY)', 'type':'date', "class":"form-control"}), label= "")
    in_stock = forms.BooleanField(required=False, label="Available?", initial=False)
    #author = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of the author", "class":"form-control"}), label= "", max_length=200)

    class Meta:
        model = Book
        #exclude = ('user',)
        fields = ('title', 'author', 'published_date', 'in_stock',)

class EditBookForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Title of the book", "class":"form-control"}), label= "", max_length=150)
    #published_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'Published date (YYYY-MM-DD)', "class":"form-control"}), label= "", input_formats=['%Y-%m-%d'])
    published_date = forms.DateField(required=True, widget=forms.DateInput(format = ('%d/%m/%Y') ,attrs={'placeholder': 'Published date (DD-MM-YYYY)', 'type':'date', "class":"form-control"}), label= "")
    in_stock = forms.BooleanField(required=False, label="Available?", initial=False)
    #author = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of the author", "class":"form-control"}), label= "", max_length=200)

    class Meta:
        model = Book
        #exclude = ('user',)
        fields = ('title', 'author', 'published_date', 'in_stock',)