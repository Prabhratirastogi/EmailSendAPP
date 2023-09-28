
from django.urls import path
from .views import EmailSendView

urlpatterns = [
    path('send-mail/', EmailSendView.as_view(), name='send-email'),
]
