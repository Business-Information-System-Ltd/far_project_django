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


def validate_location_code(value: str) -> str:
    """Validate location code."""
    return validate_code_pattern(
        value=value,
        pattern=r"^[A-Z0-9\-_]+$",
        field_label="Location code",
    )


def validate_location_name(value: str) -> str:
    """Validate location name."""
    value = trim_text(value)
    
    if not value:
        raise serializers.ValidationError("Location name is required.")
    
    return value


def validate_location_type(value: str) -> str:
    """Validate location type - convert to proper case (First letter uppercase, rest lowercase)."""
    if not value:
        return value
    
    value = value.lower()
    value = value.capitalize()
    
   
    valid_types = ['Warehouse', 'Office', 'Store', 'Factory', 'Branch']
    if value not in valid_types:
        raise serializers.ValidationError(
            f"Location type must be one of: {', '.join(valid_types)}"
        )
    
    return value