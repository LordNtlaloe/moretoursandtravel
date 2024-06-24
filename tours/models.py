from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date

class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(unique=True, null=True, max_length=200)
    bio = models.TextField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(null=True, default="profile.jpeg")

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.first_name

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField(null=True)
    category_image = models.CharField(max_length=200, null=True, default="background.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    district = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    cover_image = models.ImageField(null=True, default='background.jpg')   
    duration_days = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    overall_ratings = models.IntegerField(null=True )
    hospitality = models.IntegerField(null=True )
    service = models.IntegerField(null=True )
    pricing = models.IntegerField(null=True )
    tour_image = models.ImageField(null=True )
    message = models.TextField(null=True)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message[0:50]

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        bookingitems = self.bookingitem_set.all()
        total = sum([item.get_total for item in bookingitems])
        return total
    
    @property
    def get_cart_items(self):
        bookingitems = self.bookingitem_set.all()
        total = sum([item.quantity for item in bookingitems])
        return total
    
    @property
    def shipping(self):
        shipping = True
        return shipping


class BookingItem(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    tour_date = models.DateField(default=date.today)  # Use date.today for DateField
    num_people = models.IntegerField(default=1)
    tour_duration = models.IntegerField(default=1)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)  # Use datetime.now for DateTimeField
    updated_at = models.DateTimeField(default=datetime.now)  # Use datetime.now for DateTimeField

    def __str__(self):
        return self.tour.name

    @property
    def get_total(self):
        return self.tour.price * self.quantity

class UserDetails(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address