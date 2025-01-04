from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('departments.urls')),
    path('', include('books.urls')),
    path('', include('category.urls')),
    path('', include('patron.urls')),
    path('', include('borrowed_book.urls')),
    path('', include('tracking.urls')),
    path('accounts/', include('accounts.urls'))
]