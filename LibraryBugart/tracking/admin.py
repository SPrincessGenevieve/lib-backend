from django.contrib import admin
from .models import Tracking

@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ('tracking_number','id_number', 'patron_fname', 'patron_lname', 'request_book', 'request_status', 'patron_due_date')
    search_fields = ('patron_fname__patron_fname', 'patron_lname__patron_lname', 'request_book__title', 'request_status')
