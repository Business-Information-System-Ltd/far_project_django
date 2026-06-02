class LocationFieldMeta:
    
    FIELD_RULES = {
        "location_code": {
            "required": True,
            "max_length": 10,
            "pattern": r"^[A-Z0-9\-_]+$",
        },
        "location_name": {
            "required": True,
            "max_length": 100,
        },
        "location_type": {
            "required": False,
            "max_length": 20,
            # "choices": ["WAREHOUSE", "OFFICE", "STORE", "FACTORY", "BRANCH"],
            # "format": "First letter uppercase, rest lowercase",
        },
    }
    
    @classmethod
    def get_field_meta(cls, field_name):
        return cls.FIELD_RULES.get(field_name, {})