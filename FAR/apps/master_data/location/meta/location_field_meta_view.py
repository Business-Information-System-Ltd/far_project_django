from rest_framework.views import APIView
from rest_framework.response import Response
from apps.master_data.location.meta.location_meta import LocationFieldMeta


class LocationFieldMetaView(APIView):
    
    def get(self, request, field_name):
        meta = LocationFieldMeta.get_field_meta(field_name)
        
        if not meta:
            return Response({"error": "Field not found"}, status=404)
        
        return Response({
            "field": field_name,
            "meta": meta
        })