from rest_framework import viewsets
from apps.master_data.location.models.location_models import Location
from apps.master_data.location.api.serializers.location_serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):  
    queryset = Location.objects.select_related('parent_location', 'country').all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username if self.request.user.is_authenticated else "System")


    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username if self.request.user.is_authenticated else "System")

 