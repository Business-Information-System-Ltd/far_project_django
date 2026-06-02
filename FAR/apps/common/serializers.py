
from rest_framework import serializers 
from apps.master_data.branch.models.branch_models import Branch
# Country import is unused here, but kept if you need it for nested fields
from apps.master_data.country.models.country_models import Country

from apps.common.validators.validators import (
    trim_text, 
    validate_code_pattern, 
)

class BranchSerializer(serializers.ModelSerializer): 

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

    def create(self, validated_data):
        # ModelSerializer already provides a default create method.
        # You only need to override it if you have custom logic.
        return super().create(validated_data)