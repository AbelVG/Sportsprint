from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cloth/<int:pk>/', views.cloth_detail, name='cloth_detail'),
    path('add-to-cart/<int:cloth_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('quote/', views.send_quote, name='send_quote'),
]
