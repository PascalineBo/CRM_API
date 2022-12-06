from django.db import models
from core.models import MotherModel
from customer.models import Customer


class Contract(MotherModel):
    contract_customer = models.ForeignKey(Customer,
                                          on_delete=models.CASCADE,
                                          related_name="customer")
    price = models.FloatField()
    signed = models.BooleanField(default=False)
    payment_due = models.DateTimeField()  # DateTimeField chosen, because
    # it may later be used by the Finance Department Database
