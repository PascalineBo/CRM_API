from django.conf import settings
from core.models import MotherModel
from django.db import models

# Create your models here.
class Customer(MotherModel):
    active_customer = models.BooleanField()
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=17)
    customer_adress = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='sales_contact')

    def __str__(self):
        return str(self.company_name)