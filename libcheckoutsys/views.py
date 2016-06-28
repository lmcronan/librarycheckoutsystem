from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.shortcuts import render
import cgi

from .models import Book

def index(request):
	context = {}
	return render(request, 'index.html', context)

def books(request):
	book_list = Book.objects.order_by('title')
	context = {
		'book_list': book_list,
	}
	return render(request, 'books.html', context)

def overdue(request):
	overdue_list = Book.objects.filter(status='O').order_by('title')
	context = {
		'overdue_list': overdue_list,
	}
	return render(request, 'overdue.html', context)

def add_book(request):
	context = {}
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		print title
		b = Book(title=title, author=author, borrower='', status='B', amount=0)
		b.save()

	return render(request, 'add_book.html', context)	
	
def book_added(request):
	context = {}
	return render(request, 'book_added.html', context)
	

def fines(request):	
	return HttpResponse("Fine page")

def borrowerslist(request):
	context = {}
	return render(request, 'borrowerslist.html', context)
	
def borrowers_list_of_books(request):
	if request.method == 'POST':
		name_input = request.POST['name_textarea']
	books_borrowed = Book.objects.filter(borrower=name_input).order_by('title')
	context = {
		'books_borrowed': books_borrowed,
	}
	return render(request, 'borrowers_list_of_books.html', context)
