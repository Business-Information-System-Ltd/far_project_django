from django.db import models
<<<<<<< HEAD
from apps.master_data.branch.models.branch_models import Branch  
from apps.master_data.department.models.department_models import Department  
class Custodian(models.Model):
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,  blank=True)
=======
from apps.master_data.department.models.department_models import Department
from apps.master_data.branch.models.branch_models import Branch

class Custodian(models.Model):
    
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,  blank=True)
>>>>>>> afc35d137644c422519aa9463502b018c0d42f25
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    
    custodian_id = models.AutoField(primary_key=True)
    
    custodian_name = models.CharField(max_length=100,null = False)
    custodian_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    can_hold_assets = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    class Meta:
        db_table = 'custodian'
        
    def __str__(self):
        return self.custodian_name
        
        

        