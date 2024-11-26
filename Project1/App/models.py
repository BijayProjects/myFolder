from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccount(models.Model):
    User_Name = models.CharField(max_length=100)
    User_Email = models.EmailField()
    User_Password = models.CharField(max_length=200)

    def __str__(self):
        return self.User_Name


# class User(AbstractUser):
#     is_admin = models.BooleanField('is admin', default=False)
#     is_customer = models.BooleanField('is admin', default=False)
#     is_employee = models.BooleanField('is admin', default=False)
