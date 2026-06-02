

from rest_framework import serializers 
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.country.models.country_models import Country




    




import apps.common.validators.validators






class BranchSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source = 'country.country_name', read_only=True)

    class Meta:
        model = Branch
        fields = "__all__"

    
   
    def validate_branch_code(self, value):
        return validate_branch_code_format(value)

    

   