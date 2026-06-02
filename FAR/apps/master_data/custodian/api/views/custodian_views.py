from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.master_data.custodian.models.custodian_models import Custodian
from apps.master_data.custodian.api.serializers.custodian_serializers import CustodianSerializer

class CustodianViewSet(viewsets.ModelViewSet):
    queryset = Custodian.objects.all()
    serializer_class = CustodianSerializer

    def create(self, request, *args, **kwargs):
        print("--- Frontend Payload ---")
        print(request.data)
        
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            print("--- Serializer Validation Errors ---")
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # ✅ status ရပြီ
            
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # ✅ status ရပြီ