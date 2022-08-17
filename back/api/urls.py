from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-details'),
    path('shipments/', views.ShipmentList.as_view(), name='shipment-list'),
    path('shipments/<int:pk>/', views.ShipmentDetail.as_view(), name='shipment-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
