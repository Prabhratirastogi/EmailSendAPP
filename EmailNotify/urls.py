
from django.urls import path
from .views import EmailSendView
from .views import PantryItemListCreateView, PantryItemRetrieveUpdateDestroyView, PantryOrderCreateView, PantryOrderListView

urlpatterns = [
    path('send-mail/', EmailSendView.as_view(), name='send-email'),
    path('pantry-items/', PantryItemListCreateView.as_view(), name='pantry-item-list-create'),
    path('pantry-items/<int:pk>/', PantryItemRetrieveUpdateDestroyView.as_view(), name='pantry-item-retrieve-update-destroy'),
    path('pantry-orders/', PantryOrderCreateView.as_view(), name='create-pantry-order'),
    path('pantry-orders/all/', PantryOrderListView.as_view(), name='list-pantry-orders'),
]
