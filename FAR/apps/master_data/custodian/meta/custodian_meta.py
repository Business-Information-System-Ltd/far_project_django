class CustodianFieldMeta:

    FIELD_RULES = {
        "custodian_code": {
            "required": True,
            "max_length": 10,
            "pattern": "^[A-Z0-9\\-_]+$", 
        },
        "custodian_name": {
            "required": True,
            "max_length": 100,
        },
        "custodian_type": {
            "required": True,
            "max_length": 50,
        },
        "phone": {
            "required": False,
            "max_length": 20,
        },
        "email": {
            "required": False,
            "max_length": 100,
        },
    }

    @classmethod
    def get_field_meta(cls, field_name):
        return cls.FIELD_RULES.get(field_name, {})