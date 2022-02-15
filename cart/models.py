from django.db import models

from accounts.models import User


class Cart(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
