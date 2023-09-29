
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import EmailSerializer
# from django.core.mail import send_mail
# # Create this task in the next step

# class EmailSendView(APIView):
#     def post(self, request, format=None):
#         serializer = EmailSerializer(data=request.data)
#         if serializer.is_valid():
#             # send_email.delay(
#             #     serializer.validated_data['subject'],
#             #     serializer.validated_data['message'],
#             #     serializer.validated_data['recipient']
#             # )
#             send_mail(  # Use the send_email function directly
#                 serializer.validated_data['subject'],
#                 serializer.validated_data['message'],
#                 serializer.validated_data['recipient'],
#                 fail_silently=False,
#             )
#             return Response("Email sent asynchronously.", status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailSerializer, PantryItemSerializer, PantryOrderSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from .models import PantryItem, PantryOrder
# views for EmailSending
class EmailSendView(APIView):
    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            recipient = serializer.validated_data['recipient']

            send_mail(
                subject,
                message,
                '',  # Sender's email
                recipient,  
                fail_silently=False,
            )
            return Response("Email sent successfully.", status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#views for PantryItem 
class PantryItemListCreateView(generics.ListCreateAPIView):
    queryset = PantryItem.objects.all()
    serializer_class = PantryItemSerializer

class PantryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PantryItem.objects.all()
    serializer_class = PantryItemSerializer

# views for PantryOrder


class PantryOrderCreateView(generics.CreateAPIView):
    queryset = PantryOrder.objects.all()
    serializer_class = PantryOrderSerializer
    
class PantryOrderListView(generics.ListAPIView):
    queryset = PantryOrder.objects.all()
    serializer_class = PantryOrderSerializer


