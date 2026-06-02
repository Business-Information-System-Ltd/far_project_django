from rest_framework import serializers
from apps.master_data.location.validators.location_validators import validate_location_code, validate_location_name, validate_location_type
from apps.master_data.location.models.location_models import Location
from apps.master_data.country.api.serializers.country_serializers import CountrySerializer
from apps.master_data.country.models.country_models import Country

class LocationSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
=======


    full_path = serializers.SerializerMethodField()
    full_location_code = serializers.SerializerMethodField()
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source="country",
        write_only=True
    )

    class Meta:
        model = Location
        fields = '__all__'

    def get_full_path(self, obj):
        if obj.parent_location:
            return f"{self.get_full_path(obj.parent_location)} >> {obj.location_name}"
        return obj.location_name
    
    def get_full_location_code(self, obj):
        current_code = obj.location_code if obj.location_code else ""
        
        if obj.parent_location:
            parent_code_path = self.get_full_location_code(obj.parent_location)
            return f"{parent_code_path}-{current_code}" if parent_code_path and current_code else parent_code_path or current_code
            
        return current_code

    
>>>>>>> afc35d137644c422519aa9463502b018c0d42f25
    
    
    def validate_location_code(self, value):
        """Validate location code - only uppercase, numbers, hyphens, underscores"""
        return validate_location_code(value)
    
    def validate_location_name(self, value):
        """Validate location name - required and trimmed"""
        return validate_location_name(value)
    
    def validate_location_type(self, value):
        """Validate location type - convert to proper case (first letter uppercase, rest lowercase)"""
        return validate_location_type(value)
<<<<<<< HEAD
=======

>>>>>>> afc35d137644c422519aa9463502b018c0d42f25
