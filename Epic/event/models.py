from django.db import models
from django.conf import settings
from core.models import MotherModel
from customer.models import Customer
from contract.models import Contract
from django.db import models
from django.utils import timezone


# Create your models here.
class Event(MotherModel):
    FUTURE = 'FUTURE'
    ONGOING = 'ONGOING'
    ENDED = 'ENDED'

    EVENT_STATUS = (
        (FUTURE, 'Future'),
        (ONGOING, 'Ongoing'),

        (ENDED, 'Ended')
    )

    related_contract = models.ForeignKey(Contract,
                                        on_delete=models.CASCADE,
                                        null=False)
    event_name = models.CharField(max_length=50)
    event_date = models.DateTimeField(max_length=12)
    event_customer = models.ForeignKey(to=Customer,
                                      on_delete=models.CASCADE,
                                      related_name='event_customer',
                                      null=False
                                      )
    event_place = models.CharField(max_length=200)
    event_support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                                on_delete=models.CASCADE,
                                                related_name='event_support_contact',
                                                )
    event_sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                            on_delete=models.CASCADE,
                                            related_name='event_sales_contact',
                                            )
    event_status = models.CharField(max_length=30,
                                    choices=EVENT_STATUS,
                                    verbose_name='status',
                                    default=FUTURE)
    notes = models.CharField(max_length=2048)
    attendees = models.IntegerField()

    def __str__(self):
        return str(self.event_name)