import json
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from . models import * 

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

	items = []
	booking = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	bookingItems = booking['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:	
			if(cart[i]['quantity']>0): #items with negative quantity = lot of freebies  
				bookingItems += cart[i]['quantity']

				tour = Tour.objects.get(id=i)
				total = (tour.price * cart[i]['quantity'])

				booking['get_cart_total'] += total
				booking['get_cart_items'] += cart[i]['quantity']

				item = {
				'id':tour.id,
				'tour':{'id':tour.id,'name':tour.name, 'price':tour.price, 
				'imageURL':tour.imageURL}, 'quantity':cart[i]['quantity'],
				'digital':tour.digital,'get_total':total,
				}
				items.append(item)

				if tour.digital == False:
					booking['shipping'] = True
		except:
			pass
			
	return {'bookingItems':bookingItems ,'booking':booking, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user
		booking, created = Booking.objects.get_or_create(customer=customer, completed=False)
		items = booking.bookingitem_set.all()
		bookingItems = booking.get_cart_items
	else:
		cookieData = cookieCart(request)
		bookingItems = cookieData['bookingItems']
		booking = cookieData['booking']
		items = cookieData['items']

	return {'bookingItems':bookingItems ,'booking':booking, 'items':items}

	
def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	booking = Booking.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		tour = Tour.objects.get(id=item['id'])
		bookingItem = BookingItem.objects.create(
			tour=tour,
			booking=booking,
			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
		)
	return customer, booking

def guestBooking(request, data):
    transaction_id = datetime.datetime.now().timestamp()

    first_name = data['form']['firstName']
    last_name = data['form']['lastName']
    email = data['form']['email']
    phone_number = data['form']['phoneNumber']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(email=email)
    customer.first_name = first_name
    customer.last_name = last_name
    customer.phone_number = phone_number
    customer.save()

    booking = Booking.objects.create(
        customer=customer,
        completed=False,
        transaction_id=transaction_id
    )

    for item in items:
        try:
            tour = Tour.objects.get(id=item['tour']['id'])
            BookingItem.objects.create(
                tour=tour,
                booking=booking,
                quantity=item['quantity']
            )
        except Tour.DoesNotExist:
            # Log error or handle as appropriate
            continue

    return customer, booking

def generate_invoice(booking, items):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, f"Invoice for Booking ID: {booking.id}")
    p.drawString(100, height - 120, f"Customer: {booking.user.first_name} {booking.user.last_name}")
    p.drawString(100, height - 140, f"Email: {booking.user.email}")

    y = height - 180
    for item in items:
        p.drawString(100, y, f"{item.tour.name}: M{item.tour.price}")
        y -= 20

    p.drawString(100, y - 40, f"Total: M{booking.get_cart_total}")
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer