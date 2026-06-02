from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from apps.master_data.department.meta.department_meta import DepartmentFieldMeta


class DepartmentFieldMetaView(APIView):
    
    def get(self, request, field_name):
        meta = DepartmentFieldMeta.get_field_meta(field_name)
        
        if not meta:
            return Response({"error": "Field not found"}, status=404)
        
        return Response({
            "field": field_name,
            "meta": meta
        })