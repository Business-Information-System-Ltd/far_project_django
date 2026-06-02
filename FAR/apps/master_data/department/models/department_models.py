from django.db import models


class Department(models.Model):
    
    class DepartmentType(models.TextChoices):

<<<<<<< HEAD

        OPERATIONS = 'OPERATIONS', 'Operations'
        SUPPORT = 'SUPPORT', 'Support'
=======
       
        OPERATIONS = 'OPERATIONS', 'Operations'
        SUPPORT = 'SUPPORT','Support'
>>>>>>> afc35d137644c422519aa9463502b018c0d42f25


    department_id = models.AutoField(primary_key=True)
    
    
    parent_dept = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sub_departments',
        db_column='parent_dept_id'
    )
    
    dept_code = models.CharField(max_length=20, null=True, blank=True)
    dept_name = models.CharField(max_length=100)
    dept_short_name = models.CharField(max_length=10, null=True, blank=True)
  
    
    
    dept_type = models.CharField(
        max_length=20,
        choices=DepartmentType.choices,
        default=DepartmentType.OPERATIONS
    )
    
    allow_assignment = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'department'  

    def __str__(self):
        return self.dept_name