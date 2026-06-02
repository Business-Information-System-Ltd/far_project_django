from rest_framework import serializers 
from apps.master_data.currency.models.currency_models import Currency
from apps.master_data.country.models.country_models import Country
from apps.common.validators.validators import (
     uppercase_text, 
     
     validate_country_code, )
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

    def validate_country_code(self, value): 
        return validate_country_code(value)
    
    def validate_country_name(self, value): 
        value = uppercase_text(value) 
        if not value: 
            raise serializers.ValidationError("Country name is required.") 

        return value
    

