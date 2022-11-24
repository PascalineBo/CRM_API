"""Epic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import RegisterAPIView
from customer.views import CustomerViewset
from contract.views import ContractViewset
from event.views import EventViewset


router = routers.SimpleRouter()

# /customers/   ||   /customers/{id}/
router.register('customers', CustomerViewset, basename='customer')
customers_router = routers.NestedSimpleRouter(router, 'customers', lookup='customer')

# /contracts/   ||   /contracts/{id}/
router.register('contracts', ContractViewset, basename='contract')
contracts_router = routers.NestedSimpleRouter(router, 'contracts', lookup='contract')

# /contracts/   ||   /contracts/{id}/
router.register('events', EventViewset, basename='event')
events_router = routers.NestedSimpleRouter(router, 'events', lookup='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('epic-auth/', include('rest_framework.urls')),
    path('epic/login/', TokenObtainPairView.as_view(), name='login'),
    path('epic/signup/', RegisterAPIView.as_view(), name='signup'),
    path('epic/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('epic/', include(router.urls)),
    path('epic/', include(contracts_router.urls)),
    path('epic/', include(customers_router.urls)),
]


