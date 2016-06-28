from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.books, name='books'),
    url(r'^overdue/$', views.overdue, name='overdue'),
    url(r'^add_book/$', csrf_exempt(views.add_book), name='add_book'),
   	url(r'^book_added/$', views.book_added, name='book_added'),
    url(r'^fines/$', views.fines, name='fines'),
    url(r'^borrowerslist/', csrf_exempt(views.borrowerslist), name='borrowerslist'),
    url(r'^borrowers_list_of_books/$', csrf_exempt(views.borrowers_list_of_books), name='borrowers_list_of_books'),
]