from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import User
from customer.models import Customer
from event.models import Event

class IsControlling(BasePermission):
    """Controllers must be authenticated, then have all permissions in the system"""

    def has_permission(self, request, view):
        return request.user.position == 'CONTROLLING'

    def has_object_permission(self, request, view, obj):
        return request.user.position == 'CONTROLLING'

class IsSales(BasePermission):
    """Permissions for Salespersons: shall create Customer, Contract, Event;
    shall Read all Customer, Contract, Event;
    shall Update own Customer, Contract, Event;
    """
    def has_permission(self, request, view):
        return request.user.position == 'SALES'

class IsCustomerSalesContactOrDetailsOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.id == obj.sales_contact.id

class IsContractSalesContactOrDetailsOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.position == 'SALES' or \
                   request.user.position == 'CONTROLLING'
        return request.user.id == obj.contract_customer.sales_contact.id

class IsSupport(BasePermission):
    """Permissions for Supportpersons: shall create Customer, Contract, Event;
        shall Read all Customer, Contract, Event;
        shall Update own Customer, Contract, Event;
        """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.position == 'SUPPORT'
        return request.user.id == obj.event_support_contact.id

# class IsEventSupportOrReadOnly(BasePermission):

    # def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
            # return request.user.position == 'SUPPORT'
        # return request.user.id == obj.event_support_contact.id

class IsEventSalesOrControllerOrEventSupport(BasePermission):
    """Permissions for Salespersons: shall create Customer, Contract, Event;
    shall Read all Customer, Contract, Event;
    shall Update own Customer, Contract, Event;
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.position == 'CONTROLLING' or \
                   request.user.position == 'SALES' or \
                   request.user.position == 'SUPPORT'
        customer_id = request.POST['event_customer'] # checks the customer related to the event
        #created (only Sales in charge of that customer may create an event for them)
        customer = Customer.objects.filter(id=customer_id) # filter returns a list
        #with one element
        event_id = view.kwargs.get('pk')
        event = Event.objects.filter(id=event_id)# filter returns a list
        #with one element
        if len(event) >= 1:
            return request.user.id == customer[0].sales_contact.id or \
                   request.user.position == 'CONTROLLING' or \
                   request.user.id == event[0].event_support_contact.id # checks the Supportsperson related
                   # to the event, for PUT Request purpose
        return request.user.id == customer[0].sales_contact.id or \
               request.user.position == 'CONTROLLING'


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.position == 'CONTROLLING' or \
                   request.user.position == 'SALES' or \
                   request.user.position == 'SUPPORT'
        return request.user.id == obj.event_customer.sales_contact.id or \
               request.user.position == 'CONTROLLING' or \
               request.user.id == obj.event_support_contact.id