import re
from typing import Optional
from rest_framework import serializers


def trim_text(value: Optional[str]) -> Optional[str]:
    """Strip leading and trailing spaces from a string."""
    if value is None:
        return value
    if not isinstance(value, str):
        raise serializers.ValidationError("Value must be a string.")
    return value.strip()


def uppercase_text(value: Optional[str]) -> Optional[str]:
    """Convert text to uppercase."""
    if value is None:
        return value
    if not isinstance(value, str):
        raise serializers.ValidationError("Value must be a string.")
    return value.upper()


def trim_upper_text(value: Optional[str]) -> Optional[str]:
    """Trim then uppercase text."""
    value = trim_text(value)
    return uppercase_text(value)


def validate_code_pattern(
    value: str,
    pattern: str = r"^[A-Z0-9\-_]+$",
    field_label: str = "Code",
    normalize: bool = True,
) -> str:
    """Validate a generic code field."""
    if normalize:
        value = trim_upper_text(value)
    
    if not value:
        raise serializers.ValidationError(f"{field_label} is required.")
    
    if not re.match(pattern, value):
        raise serializers.ValidationError(f"{field_label} format is invalid.")
    
    return value


def validate_department_code(value: str) -> str:
    """Validate department code."""
    return validate_code_pattern(
        value=value,
        pattern=r"^[A-Z0-9\-_]+$",
        field_label="Department code",
    )


def validate_department_name(value: str) -> str:
    """Validate department name."""
    value = trim_text(value)
    
    if not value:
        raise serializers.ValidationError("Department name is required.")
    
    return value