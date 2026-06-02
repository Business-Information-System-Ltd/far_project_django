
# from rest_framework import serializers
# from apps.master_data.custodian.models.custodian_models import Custodian

# class CustodianSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Custodian
#         fields = '__all__'

from rest_framework import serializers 
from apps.master_data.custodian.models.custodian_models import Custodian 

from apps.common.validators.validators import (
    validate_custodian_code,
    validate_custodian_name,
)

class CustodianSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Custodian
        fields = "__all__"

    def validate_custodian_code(self, value): 
       
        return validate_custodian_code(value)
    
    def validate_custodian_name(self, value): 
        return validate_custodian_name(value, required=True)

    def create(self, validated_data):
        return Custodian.objects.create(**validated_data)