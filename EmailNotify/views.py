
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
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailSerializer
from django.core.mail import send_mail

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
