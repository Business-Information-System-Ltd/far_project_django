class CountryFieldMeta:

    FIELD_RULES = {
        "country_code": {
            "required": True,
            "max_length": 3,
            "min_length": 3,
            "pattern": "^[A-Z]{3}$",
            "help_text": "ISO 3166-1 alpha-3 code (e.g., MMR, THA).",
        },
        "country_name": {
            "required": True,
            "max_length": 100,
            "help_text": "Official name of the country.",
        },
        "iso_numeric": {
            "required": False,
            "max_length": 3,
            "pattern": "^[0-9]{3}$",
            "help_text": "ISO 3166-1 numeric code.",
        },
        "is_active": {
            "required": False,
            "default": True,
        }
    }

    @classmethod
    def get_field_meta(cls, field_name):
        return cls.FIELD_RULES.get(field_name, {})