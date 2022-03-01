from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=100)




# If token needs to be Generated Automatically on user creation.
# This Signal creates Auth Token for User
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
