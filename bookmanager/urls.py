from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('publisher_list/',views.publisher_list),
    url('publisher_add/',views.publisher_add),
    url('publisher_del/',views.publisher_del),
    url('publisher_edit/',views.publisher_eidt),

    url('book_list/',views.book_list),
    url('book_add/',views.book_add),
    url('book_del/',views.book_del),
    url('book_edit/',views.book_edit),

    url('author_list/',views.author_list),
    url('author_add/',views.author_add),
    url('author_del/',views.author_del),
    url('author_edit/',views.author_edit),

    url('search/',views.serach),
    url('book_det/',views.book_det),
]
