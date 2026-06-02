from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.currency.api.serializers.currency_serializers import CurrencySerializer
from rest_framework import viewsets

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer