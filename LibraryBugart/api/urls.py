from rest_framework.routers import DefaultRouter
from django.urls import path, include
from departments.views import DepartmentViewSet
from books.views import BookViewSet
from category.views import CategoryViewSet
from patron.views import PatronViewSet
from borrowed_book.views import BorrowedBookViewSet
from tracking.views import TrackingViewSet
from accounts.views import AccountViewSet

# Create the router and register your viewsets
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'books', BookViewSet, basename='book')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'patrons', PatronViewSet, basename='patron')
router.register(r'borrowed-books', BorrowedBookViewSet, basename='borrowedbook')
router.register(r'tracking', TrackingViewSet, basename='tracking')
router.register(r'accounts', AccountViewSet, basename='account')

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
