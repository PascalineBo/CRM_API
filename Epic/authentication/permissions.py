from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import User

class IsControlling(BasePermission):
    """Controllers must be authenticated, then have all permissions in the system"""

    def has_object_permission(self, request, view, obj):
        return bool(request.user.position == 'CONTROLLING')

class IsSales(BasePermission):
    """Permissions for Salespersons: shall create Customer, Contract, Event;
    shall Read all Customer, Contract, Event;
    shall Update own Customer, Contract, Event;
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user.position == 'SALES')
        else:
            return False

class IsCustomerSalesContactOrDetailsOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        customer_id = view.kwargs['pk']
        return bool(request.user.id == obj.sales_contact.id)

class IsSupport(BasePermission):
    """Permissions for Supportpersons: shall create Customer, Contract, Event;
        shall Read all Customer, Contract, Event;
        shall Update own Customer, Contract, Event;
        """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.position == 'SUPPORT')
    ...