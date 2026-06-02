
from apps.master_data.country.models.country_models import Country
from apps.master_data.country.api.serializers.country_serializers import CountrySerializer
from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
