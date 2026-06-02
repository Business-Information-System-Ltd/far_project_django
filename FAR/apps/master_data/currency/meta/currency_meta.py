class CurrencyFieldMeta:

    FIELD_RULES = {
        "currency_code": {
            "required": True,
            "max_length": 3,
            "pattern": "^[A-Z0-9\\-_]+$",  
        },
        "currency_name": {
            "required": True,
            "max_length": 50,
        },
        "currency_symbol": {
            "required": False,
            "max_length": 10,
        },
        "decimal_places": {
            "required": False,
        },
    }

    @classmethod
    def get_field_meta(cls, field_name):
        return cls.FIELD_RULES.get(field_name, {})