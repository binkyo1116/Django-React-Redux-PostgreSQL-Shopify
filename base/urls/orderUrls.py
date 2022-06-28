from django.urls import path
from base.views import orderViews as views

urlpatterns = [
    #path is already /api/orders by default so it is empty
    path('', views.getOrders, name='orders'),
    path('add/', views.addOrderItems, name='order-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]