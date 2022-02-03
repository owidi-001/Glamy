from django.contrib.auth.models import AbstractUser
from django.db import models

# Generates auth token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# local modules
from .managers import UserManager


def upload(instance, filename):
    return f"media/{instance.user.id}/avatar/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, null=False, blank=False, unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=upload)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]
    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.email}"


"""
 generate authentication  token after a user has been created and send him/her an email
"""


@receiver(post_save, sender=User)
def create_auth_token(sender=None, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_token = models.IntegerField(null=True)
    reset_token = models.CharField(max_length=100)