# from rest_framework import serializers 
# # from apps.master_data.branch.models.branch_models import Branch
# from apps.master_data.currency.models.currency_models import Currency

# class CurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Currency
#         fields = "__all__"


from rest_framework import serializers 
from apps.master_data.currency.models.currency_models import Currency

from apps.common.validators.validators import (
    validate_currency_code,
    validate_currency_name,
)

class CurrencySerializer(serializers.ModelSerializer): 

    class Meta:
        model = Currency
        fields = "__all__"

    def validate_currency_code(self, value): 

        return validate_currency_code(value, required=True)
    
    def validate_currency_name(self, value): 
        return validate_currency_name(value, required=True)

    def create(self, validated_data):
        return Currency.objects.create(**validated_data)