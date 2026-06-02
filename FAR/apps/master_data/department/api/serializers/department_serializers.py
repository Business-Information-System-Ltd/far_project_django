from rest_framework import serializers
from apps.master_data.department.models import Department
from apps.master_data.department.models.department_models import Department
from apps.common.validators.validators import trim_text, validate_code_pattern




class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = "__all__"
    
    def validate_dept_code(self, value):
        return validate_code_pattern(
            value=value,
            pattern=r"^[A-Z0-9\-_]+$",
            field_label="Department code",
        )
    
    def validate_dept_name(self, value):
        value = trim_text(value)
        
        if not value:
            raise serializers.ValidationError("Department name is required.")
        
        return value