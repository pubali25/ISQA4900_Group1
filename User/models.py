from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPE = [
    (1, 'User'),
    (2, 'Instructor'),
]

class User(AbstractUser):
    cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
    user_type = models.SmallIntegerField(choices=USER_TYPE, null=False, default=1)
    address1 = models.CharField(blank=True, default=' ', max_length=50, null=True)
    address2 = models.CharField(blank=True, default=' ', max_length=50, null=True)
    city = models.CharField(blank=True, default=' ', max_length=50, null=True)
    state = models.CharField(blank=True, default=' ', max_length=2, null=True)
    zipcode = models.CharField(blank=True, default=' ', max_length=5, null=True)

class NewsUsers(models.Model):
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "NewsUser"
        verbose_name_plural = "NewsUsers"
        def __str__(self):
            return self.email

# Create your models here.
