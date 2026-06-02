from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class ApiRootView(APIView):
    def get(self, request):
        return Response({
            "branches": request.build_absolute_uri("branches/"),
            "countries": request.build_absolute_uri("countries/"),
            "currencies": request.build_absolute_uri("currencies/"),
            "locations": request.build_absolute_uri("locations/"),
            "departments": request.build_absolute_uri("departments/"),
            "custodians": request.build_absolute_uri("custodians/"),
        })