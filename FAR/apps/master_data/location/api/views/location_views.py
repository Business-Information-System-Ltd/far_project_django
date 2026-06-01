from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from apps.master_data.location.models.location_models import Location
from apps.master_data.location.api.serializers.location_serializers import LocationSerializer
from apps.common.utils.search.search_engine import SearchEngine
from django_filters.rest_framework import DjangoFilterBackend
from apps.reference.pagination.global_paginations import StandardResultsSetPagination


class LocationViewSet(viewsets.ModelViewSet):  
    queryset = Location.objects.select_related('parent_location', 'country').all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username if self.request.user.is_authenticated else "System")


    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user.username if self.request.user.is_authenticated else "System")

    pagination_class = StandardResultsSetPagination

    filterset_fields = ["is_active"]  
    search_fields = ["location_name", "location_code", "full_path"]


    # Filter:is_active
        
    def get_queryset(self):
        queryset = super().get_queryset()

        is_active = self.request.query_params.get("is_active")

        if is_active is not None:
            if is_active.lower() == "true":
                queryset = queryset.filter(is_active=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(is_active=False)

        search = self.request.query_params.get("search")
        if search:
            if ":" in search:
                field, value = search.split(":", 1)
                if field == "location_code":
                    queryset = queryset.filter(location_code__iexact=value)
                elif field == "location_name":
                    queryset = queryset.filter(location_name__icontains=value)
                elif field == "location_type":
                    queryset = queryset.filter(location_type__icontains=value)
                elif field == "city":
                    queryset = queryset.filter(city__icontains=value)
                elif field == "region":
                    queryset = queryset.filter(region__icontains=value)
            else:
                queryset = queryset.filter(
                    Q(location_code__icontains=search) |
                    Q(location_name__icontains=search) |
                    Q(location_type__icontains=search) |
                    Q(city__icontains=search) |
                    Q(region__icontains=search)
                )
        
        return queryset