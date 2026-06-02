from rest_framework import serializers
from apps.master_data.location.models.location_models import Location

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Location
        fields = "__all__"
    
    def validate_location_code(self, value):
        """Validate location code - only uppercase, numbers, hyphens, underscores"""
        return validate_location_code(value)
    
    def validate_location_name(self, value):
        """Validate location name - required and trimmed"""
        return validate_location_name(value)
    
    def validate_location_type(self, value):
        """Validate location type - convert to proper case (first letter uppercase, rest lowercase)"""
        return validate_location_type(value)
