# your_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User  # Replace with your User model if it's custom
from .models import Profile

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Check if the user was newly created
        send_mail(
            'Registration Successful',
            f'Hi {instance.username}, your registration was successful!',
            settings.EMAIL_HOST_USER,  # Sender email (configured in settings.py)
            [instance.email],  # Recipient email
            fail_silently=False,
        )


# your_app/signals.py

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.models import User  # Default User model
# from .models import Product

# @receiver(post_save, sender=Product)
# def notify_all_users(sender, instance, created, **kwargs):
#     if created:  # Only notify when a new product is created
#         users = User.objects.all()  # Get all users
#         for user in users:
#             send_mail(
#                 'New Product Added',
#                 f'Hello {user.username}, a new product "{instance.name}" has been added to the store.',
#                 settings.EMAIL_HOST_USER,  # Sender email (configured in settings.py)
#                 [user.email],  # Recipient email (user's email)
#                 fail_silently=False,
#             )


# your_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from django.contrib.auth.models import User
from .models import Product


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Signal to create a Profile for every new User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the profile when the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Product, Profile

# Function to send SMS via Twilio
def send_sms(phone_number, product_name):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    # Send SMS using Twilio
    client.messages.create(
        body=f"New product added: {product_name}. Check it out!",
        from_=settings.TWILIO_PHONE_NUMBER,  # Your Twilio phone number
        to=phone_number,  # Recipient's phone number
    )

# Receiver to notify users via email and SMS when a new product is created
@receiver(post_save, sender=Product)
def notify_all_users(sender, instance, created, **kwargs):
    if created:  # Only notify when a new product is created
        # Get all users
        users = User.objects.all()
        
        for user in users:
            # Send email notification
            send_mail(
                'New Product Added',
                f'Hello {user.username}, a new product "{instance.name}" has been added to the store.',
                settings.EMAIL_HOST_USER,  # Sender email (configured in settings.py)
                [user.email],  # Recipient email (user's email)
                fail_silently=False,
            )
            
            # Send SMS notification if the user has a phone number
            try:
                profile = user.profile  # Try to get the user's profile
                if profile.phone_number:  # Check if the user has a phone number
                    send_sms(profile.phone_number, instance.name)
            except Profile.DoesNotExist:
                # Handle the case where the user does not have a profile
                continue
