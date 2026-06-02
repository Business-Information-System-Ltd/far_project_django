from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.master_data.custodian.models.custodian_models import Custodian
from apps.master_data.custodian.api.serializers.custodian_serializers import CustodianSerializer

class CustodianViewSet(viewsets.ModelViewSet):
    queryset = Custodian.objects.all()
    serializer_class = CustodianSerializer

    