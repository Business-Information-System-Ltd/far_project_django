from rest_framework import serializers 
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.country.models.country_models import Country
from apps.master_data.country.api.serializers.country_serializers import CountrySerializer
from apps.common.validators.validators import (
     trim_text, 
     validate_code_pattern, 
      )

class BranchSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        source="country",
        write_only=True
    )

    class Meta:
        model = Branch
        fields = "__all__"

    
    def validate_branch_code(self, value): 
        return validate_code_pattern( 
           value=value, 
            pattern=r"^[A-Z0-9\-_]+$", 
          field_label="Branch code", 
          )
    
    def validate_branch_name(self, value): 
        value = trim_text(value) 
        if not value: 
          raise serializers.ValidationError("Branch name is required.") 
        return value
    
    def validate_city(self, value): 
        return trim_text(value)
    

   