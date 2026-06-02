from apps.common.validators.validators import (
    trim_text,
    validate_code_pattern,
)


def validate_custodian_code(value):
    return validate_code_pattern(
        value=value,
        pattern=r"^[A-Z0-9\-_]+$",
        field_label="Custodian code",
    )


def validate_custodian_name(value):
    value = trim_text(value)
    if not value:
        raise ValueError("Custodian name is required.")
    return value


def validate_phone(value):
    return trim_text(value)


def validate_email(value):
    return trim_text(value)