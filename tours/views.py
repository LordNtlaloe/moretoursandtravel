from django.shortcuts import render, redirect
from .models import Category, Customer, Gallery, Activity, Tour, Review, User, Booking, BookingItem, UserDetails, Destination
from django.db.models import Q
from .forms import UserForm, UserRegisrationForm, TourForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, HttpResponse, JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, generate_invoice, guestBooking
from urllib.parse import urlparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    booking = data['booking']
    items = data['items']

    q = request.GET.get('q', '')
    destinations = Destination.objects.all()
    tours = Tour.objects.filter(
        Q(name__icontains=q) | 
        Q(description__icontains=q) | 
        Q(category__category_name__icontains=q)
    )
    
    total_tours_count = tours.count()
    tours = tours[:6]  # Get only the first 6 tours

    categories = Category.objects.all()

    context = {
        'destinations': destinations,
        'tours': tours,
        'booking': booking,
        'categories': categories,
        'items': items,
        'bookingItems': bookingItems,
        'total_tours_count': total_tours_count  # Pass the total count to the template
    }

    return render(request, 'tours/index.html', context)


def getTour(request, name):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    tour = Tour.objects.get(name=name)
    gallery = Gallery.objects.filter(tour=tour)
    activities = Activity.objects.filter(tour=tour)
    # destination = Destination.objects.filter(tour=tour)

    reviews = tour.review_set.all().order_by('-created_at')

    if request.method == 'POST':
        Review.objects.create(
            user=request.user,
            tour=tour,
            message=request.POST.get('message')
        )
        return redirect('tour', name=tour.name)
    paginator = Paginator(reviews, 2)  # Show 6 tours per page
    page = request.GET.get('page')
    page_number = request.GET.get(page)
    page_object = paginator.get_page(page_number)
    context = {
        "page": page_object,
        'tour': tour,
        'reviews': reviews,
        'items': items,
        'bookingItems': bookingItems,
        'gallery': gallery,
        'activities': activities,
        # 'destination': destination
    }
    return render(request, 'tours/tours/tour.html', context)

def tours(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    q = request.GET.get('q', '')
    tours = Tour.objects.filter(
        Q(name__icontains=q) | 
        Q(description__icontains=q) | 
        Q(category__category_name__icontains=q)
    )
    categories = Category.objects.all()
    paginator = Paginator(tours, 6)  # Show 6 tours per page
    page = request.GET.get('page')
    page_number = request.GET.get(page)
    page_object = paginator.get_page(page_number)

    print(tours)   
    search_count = paginator.count
    context = {
        'page': page_object,
        'tours' : tours,
        'categories' : categories,
        'search_count' : search_count,
        'items' : items,
        'bookingItems' : bookingItems
    }
    return render(request, 'tours.html', context)

@login_required(login_url='login/')
def addTour(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    form = TourForm()
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            return redirect('/')
    context = { 
        'form' : form,
        'bookingItems' : bookingItems,
        'items' : items
    }
    return render(request, 'tours/tour/form.html', context)

@login_required(login_url='login/')
def updateTour(request, pk):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    tour = Tour.objects.get(id=pk)
    form = TourForm(instance=tour)

    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form,
        'items' : items,
        'bookingItems' : bookingItems
    }
    return render(request, 'tours/tour/form.html', context)

@login_required(login_url='login/')
def deleteTour(request, pk):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    tour = Tour.objects.get(id=pk)
    if request.method == 'POST':
        tour.delete()
        return redirect('/')
    return render(request, 'tours/delete.html', {'obj' : tour, 'bookingItems' : bookingItems, 'items' : items})

def explore(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    q = request.GET.get('q', '')
    tours = Tour.objects.filter(
        Q(category__category_name__icontains=q) | 
        Q(name__icontains=q) | 
        Q(description__icontains=q)
    )
    category = Category.objects.all()
    search_count = tours.count()
    context = {
        'tours' : tours,
        'category' : category,
        'search_count' : search_count,
        'items' : items,
        'bookingItems' : bookingItems
    }
    return render(request, 'tours/explore.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/', messages.success(request, 'User Login Successful'))
        else:
            messages.error(request, 'Invalid Username Or Password')
        
    return render(request, 'tours/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerUser(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    form = UserRegisrationForm()
    if request.method == 'POST':
        form = UserRegisrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Could Not Complete Registration. An Error Occured')
    return render(request, 'tours/register.html', {'form' : form, 'bookingItems' : bookingItems, 'items' : items})

@login_required(login_url='login')
def userProfile(request, pk):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    user = User.objects.get(id=pk)
    context = {
        'user' : user,
        'bookingItems' : bookingItems,
        'items' : items
    }
    return render(request, 'tours/user/profile.html', context)

@login_required(login_url='login')
def editUser(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.id)
    context = {
        'form' : form,
        'bookingItems' : bookingItems,
        'items' : items
    }
    return render(request, 'tours/user/edit-profile.html', context)

@login_required(login_url='login')
def deleteReview(request, pk):
    data = cartData(request)
    bookingItems = data['bookingItems']
    items = data['items']

    review = Review.objects.get(id=pk)
    if request.user != review.user:
        return HttpResponse('This Is A Restricted Area')
    if request.method == 'POST':
        review.delete()
        return redirect('/')
    return render(request, 'tours/delete.html', {'obj' : review, 'items' : items, 'bookingItems' : bookingItems})

def cart(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    booking = data['booking']
    items = data['items']
    context = {'items' : items, 'booking' : booking, 'bookingItems' : bookingItems}
    return render(request, 'tours/orders/cart.html', context)

def checkout(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    booking = data['booking']
    items = data['items']
    context = {'items': items, 'booking': booking, 'bookingItems': bookingItems}
    return render(request, 'tours/orders/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    tourId = data['tourId']
    action = data['action']
    print('Action:', action)
    print('Product:', tourId)

    customer = request.user
    tour = Tour.objects.get(id=tourId)
    booking, created_at = Booking.objects.get_or_create(customer=customer, completed=False)
    bookingItem, created_at = BookingItem.objects.get_or_create(booking=booking, tour=tour)

    if action == 'add':
        bookingItem.quantity += 1
    elif action == 'remove':
        bookingItem.quantity -= 1

    bookingItem.save()

    if bookingItem.quantity <= 0:
        bookingItem.delete()

    return JsonResponse('Booking was Updated', safe=False)

def processBooking(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        booking, created = Booking.objects.get_or_create(customer=customer, completed=False)
    else:
        customer, booking = guestBooking(request, data)

    total = float(data['form']['total'])
    booking.transaction_id = transaction_id

    if total == float(booking.get_cart_total):
        booking.completed = True
    booking.save()

    # if booking.delivery == True:
    #     UserDetails.objects.create(
    #         customer=customer,
    #         booking=booking,
    #         address=data['shipping']['address'],
    #         city=data['shipping']['city'],
    #         state=data['shipping']['state'],
    #         zipcode=data['shipping']['zipcode'],
    #     )

    return JsonResponse('Payment Completed', safe=False)

@login_required(login_url='login')
def bookingList(request):
    bookings = Booking.objects.all().order_by('-created_at')
    return render(request, 'tours/orders/booking-list.html', {'bookings' : bookings})

@login_required(login_url='login')
def bookingDetails(request, pk):
    booking = Booking.objects.get(id=pk)
    bookingitems = booking.bookingitem_set.all()
    context = {
        'booking' : booking,
        'bookingitems' : bookingitems
    }
    return render(request, 'tours/orders/booking-detail.html', context)

@login_required(login_url='login')
def bookingReceipt(request, pk):
    booking = Booking.objects.get(id=pk)
    bookingitems = booking.bookingitem_set.all()
    total = sum(item.get_total for item in bookingitems)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.drawString(100, 750, 'Booking Receipt')
    p.drawString(100, 735, f'Booking ID: {booking.id}')
    p.drawString(100, 720, f'Customer Name: {booking.customer}')
    p.drawString(100, 705, f'Total Amount: {total}')

    p.drawString(100, 680, 'Tour Details:')
    y = 660
    for item in bookingitems:
        p.drawString(100, y, f'Tour: {item.tour.name}')
        p.drawString(100, y - 15, f'Quantity: {item.quantity}')
        p.drawString(100, y - 30, f'Price: {item.get_total}')
        y -= 45

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='booking_receipt.pdf')

def guestBooking(request, data):
    form_data = data['form']
    shipping_data = data['shipping']
    
    # Create a new customer
    customer = Customer.objects.create(
        first_name=form_data['first_name'],
        last_name=form_data['last_name'],
        email=form_data['email'],
        phone_number=form_data['phone_number'],
    )
    
    # Create a new booking
    booking = Booking.objects.create(
        customer=customer,
        total=form_data['total'],
        address=shipping_data['address'],
        city=shipping_data['city'],
        village=shipping_data['village'],
        zipcode=shipping_data['zipcode'],
    )
    
    return customer, booking

def process_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form_data = data['form']
            cart_summary = data['cart_summary']
            
            # Ensure required fields are present
            required_fields = ['first_name', 'last_name', 'email', 'phone_number', 'total']
            for field in required_fields:
                if field not in form_data:
                    return JsonResponse({'error': f'Missing field: {field}'}, status=400)
            
            # Process the booking
            customer, booking = guestBooking(request, data)
            
            # Generate the PDF
            pdf_buffer = generate_invoice(booking, cart_summary, form_data)
            
            response = HttpResponse(pdf_buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="invoice_{booking.id}.pdf"'
            
            return response
        
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            print(f"General error: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def aboutUs(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    booking = data['booking']
    items = data['items']
    context = {
        'booking': booking,
        'items': items,
        'bookingItems': bookingItems,
    }
    return render(request, 'about.html', context)

def gallery(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    booking = data['booking']
    items = data['items']
    context = {
        'booking': booking,
        'items': items,
        'bookingItems': bookingItems,
    }
    return render(request, 'gallery.html', context)

def services(request):
    data = cartData(request)
    bookingItems = data['bookingItems']
    booking = data['booking']
    items = data['items']
    context = {
        'booking': booking,
        'items': items,
        'bookingItems': bookingItems,
    }
    return render(request, 'services.html', context)