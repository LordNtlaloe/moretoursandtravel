from django.urls import path
from . import views


# app_name = 'seek'
urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    path("delete-review/<str:pk>/", views.deleteReview, name="delete-review"),
    path("profile/<str:pk>/", views.userProfile, name="profile"),
    path("edit-profile/", views.editUser, name="edit-profile"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update-item/", views.updateItem, name='update-item'),
    path("process-payment/", views.processBooking, name="process-payment"),
    path("tours/", views.tours, name="tours"),
    path("tours/<str:name>/", views.getTour, name="tour"),
    path("add-tour/", views.addTour, name="add-tour"),
    path('edit-tour/<str:pk>/', views.updateTour, name='edit-tour'),
    path('delete-tour/<str:pk>/', views.deleteTour, name='delete-tour'),
    path('about-us', views.aboutUs, name="about-us"),
    path('gallery', views.gallery, name="gallery"),
    path('services', views.services, name="services"),
    path('process-payment/', views.process_payment, name='process-payment'),
    path('contact/', views.contact, name='contact')
]
