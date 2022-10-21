from django.contrib import admin
from .models import Book, Department,Doctors
class BookingAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_email', 'p_phone', 'doc_name', 'booking_date', 'booked_on')
admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Book,BookingAdmin)
