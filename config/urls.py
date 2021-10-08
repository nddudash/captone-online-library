"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import book_add_search_view, book_add_commit_view, book_detail, bookList_view
from custom_user.views import LoginView, LogoutView, sign_up_view
from reservations.views import reservation_view
from checkout.views import checkout_book_view, return_book_view

urlpatterns = [
    path('books/add/<int:id>', book_add_commit_view, name='AddBookView'),
    path('books/add/', book_add_search_view, name='AddBookView'),
    path('admin/', admin.site.urls),
    path('reserve/<int:id>/', reservation_view, name='reserve'),
    path('book_detail/<int:id>/', book_detail, name='book_detail_page'),
    path('login_view/', LoginView.as_view(), name='login'),
    path('logout_view/', LogoutView.as_view(), name='logout'),
    path('sign_up_view/', sign_up_view, name='sign_up'),
    path('all_books/', bookList_view, name='books_page'),
    path('checkout/<int:book_id>/', checkout_book_view, name='checkout'),
    path('return/<int:book_id>/', return_book_view, name='return'),
]
