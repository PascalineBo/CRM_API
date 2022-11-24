from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    SALES = 'SALES'
    SUPPORT = 'SUPPORT'
    CONTROLLING = 'CONTROLLING'


    POSITION_CHOICES = (
        (SALES, 'Sales'),
        (SUPPORT, 'Support'),
        
        (CONTROLLING, 'Controlling')
        )

    position = models.CharField(max_length=30,
                                choices=POSITION_CHOICES,
                                verbose_name='position')
    phone = models.CharField(max_length=17)