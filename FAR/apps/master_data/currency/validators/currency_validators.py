from apps.common.validators.validators import (
    trim_text,
    validate_code_pattern,
)


def validate_currency_code(value):
    return validate_code_pattern(
        value=value,
        pattern=r"^[A-Z0-9\-_]+$",
        field_label="Currency code",
    )


def validate_currency_name(value):
    value = trim_text(value)
    if not value:
        raise ValueError("Currency name is required.")
    return value


def validate_currency_symbol(value):
    return trim_text(value)