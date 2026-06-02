class DepartmentFieldMeta:
    """Department field metadata - same structure as BranchFieldMeta"""
    
    FIELD_RULES = {
        "dept_code": {
            "required": True,
            "max_length": 20,
            "pattern": r"^[A-Z0-9\-_]+$",
        },
        "dept_name": {
            "required": True,
            "max_length": 100,
        },
    }
    
    @classmethod
    def get_field_meta(cls, field_name: str):
        """Get field metadata."""
        return cls.FIELD_RULES.get(field_name, {})