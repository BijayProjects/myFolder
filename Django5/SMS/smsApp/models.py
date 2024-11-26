from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is Admin', default=False)
    is_customer = models.BooleanField('Is Customer', default=False)
    is_employee = models.BooleanField('Is Employee', default=False)