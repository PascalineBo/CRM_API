import logging

from rest_framework.permissions import IsAuthenticated
from authentication.permissions import \
    IsContractSalesContactOrDetailsOrReadOnly, IsControlling,\
    IsSales
from customer.models import Customer
from .models import Contract
from .serializers import ContractSerializer
from rest_framework.viewsets import ModelViewSet
from core.views import DestroyMixin
from rest_framework import filters


logging.basicConfig(filename='epic_logging.log', encoding='utf-8',
                    level=logging.INFO)


class ContractViewset(DestroyMixin, ModelViewSet):
    serializer_class = ContractSerializer

    permission_classes = [IsAuthenticated,
                          IsSales | IsControlling,
                          IsContractSalesContactOrDetailsOrReadOnly]

    # 'contract creation date' filter
    filter_backends = [filters.SearchFilter]
    search_fields = ['created_time']

    def get_queryset(self, *args, **kwargs):
        queryset = Contract.objects.all()
        customer_queryset = Customer.objects.all()

        # company name filter
        company_name = self.request.GET.get('name')
        if company_name is not None:
            company_queryset = customer_queryset.filter(
                company_name=company_name)
            if len(company_queryset) > 0:
                contract_customer = company_queryset[0]
                queryset = queryset.filter(contract_customer=contract_customer)

        # customer email filter
        customer_email = self.request.GET.get('e-mail')
        if customer_email is not None:
            customer_queryset = customer_queryset.filter(
                customer_email=customer_email)
            if len(customer_queryset) > 0:
                contract_customer = customer_queryset[0]
                queryset = queryset.filter(contract_customer=contract_customer)

        # contract price filter
        price = self.request.GET.get('price')
        if price is not None:
            queryset = queryset.filter(price=price)

        return queryset

    def destroy(self, request, model_name="contract", *args, **kwargs):
        return super().destroy(request, model_name, *args, **kwargs)
