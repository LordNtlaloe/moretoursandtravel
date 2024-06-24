from django.contrib import admin
from .models import User, Category, Tour, Review, Booking, BookingItem, UserDetails, Customer, Destination

# Register your models here.
admin.site.register(Category)
# admin.site.register(Business)
admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(BookingItem)
admin.site.register(UserDetails)
admin.site.register(Customer)
admin.site.register(Destination)
