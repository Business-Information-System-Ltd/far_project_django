class BranchFieldMeta:

    FIELD_RULES = {
        "branch_code": {
            "required": True,
            "max_length": 10,
            "pattern": "^[A-Z0-9\\-_]+$",
        },
        "branch_name": {
            "required": True,
            "max_length": 100,
        },
        "city": {
            "required": False,
        },
    }

    @classmethod
    def get_field_meta(cls, field_name):
        return cls.FIELD_RULES.get(field_name, {})