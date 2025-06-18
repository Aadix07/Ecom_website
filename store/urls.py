from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('signup/', views.signup, name='signup'),
]
