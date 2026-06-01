
from rest_framework import serializers 
from apps.master_data.custodian.models.custodian_models import Custodian 
from apps.master_data.branch.api.serializers.branch_serializers import BranchSerializer
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.department.api.serializers.department_serializers import DepartmentSerializer
from apps.master_data.department.models.department_models import Department
from apps.common.validators.validators import (
    validate_custodian_code,
    validate_custodian_name,
)

class CustodianSerializer(serializers.ModelSerializer): 
    branch = BranchSerializer(read_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(),
        source="branch",
        write_only=True
    )
    dept = DepartmentSerializer(read_only=True)
    dept_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source="dept",
        write_only=True
    )
    class Meta:
        model = Custodian
        fields = "__all__"

    def validate_custodian_code(self, value): 
       
        return validate_custodian_code(value)
    
    def validate_custodian_name(self, value): 
        return validate_custodian_name(value, required=True)

    def create(self, validated_data):
        return Custodian.objects.create(**validated_data)