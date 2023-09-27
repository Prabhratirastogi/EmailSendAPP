
# from celery import shared_task
# from django.core.mail import send_mail

# @shared_task
# def send_email():
#     subject = "Hello"
#     message = "How are you"
#     sender_email = "prabhrati.rastogi@artiligent.global"
#     recipient_email = ["prabhrati17@gmail.com", "23125prabhrati.2020@gmail.com"]  # List of recipient email addresses
#     send_mail(
#         subject,
#         message,
#         sender_email,
#         recipient_email,  # Use a list of recipient email addresses
#         fail_silently=False,
#     )

# from celery import shared_task
# from django.core.mail import send_mail

# @shared_task
# def send_email(subject, message, recipient):
#     send_mail(
#         subject,
#         message,
#         [recipient],  # List of recipient email addresses
#         fail_silently=False,
#     )
# celery -A email_project worker --loglevel=info
