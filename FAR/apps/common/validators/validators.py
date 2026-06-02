import re
from decimal import Decimal, InvalidOperation
from typing import Optional, Union
 
from rest_framework import serializers


def trim_text(value: Optional[str]) -> Optional[str]:
    """ Strip leading and trailing spaces from a string. Returns the original value if it is None.
    """ 
    if value is None: 
        return value 
    if not isinstance(value, str): 
        raise serializers.ValidationError("Value must be a string.") 
    return value.strip() 

def uppercase_text(value: Optional[str]) -> Optional[str]: 
    """ Convert text to uppercase. Returns the original value if it is None. 
    """ 
    if value is None: 
        return value 
    if not isinstance(value, str): 
        raise serializers.ValidationError("Value must be a string.") 
    return value.upper() 

def trim_upper_text(value: Optional[str]) -> Optional[str]: 
    """ Trim then uppercase text. 
    """ 
    value = trim_text(value) 
    return uppercase_text(value)


def validate_code_pattern( 
    value: str, 
    pattern: str = r"^[A-Z0-9\-_]+$", 
    field_label: str = "Code", 
    normalize: bool = True, 
) -> str:
    """ 
    Validate a generic code field. Default pattern allows uppercase letters, numbers, hyphen, underscore. 
    """ 
    if normalize: 
        value = trim_upper_text(value) 
        if not value: 
            raise serializers.ValidationError(f"{field_label} is required.") 
        if not re.match(pattern, value): 
            raise serializers.ValidationError(f"{field_label} format is invalid.") 
        return value

def validate_country_code(value: Optional[str], required: bool = False) -> Optional[str]: 
    """ Validate ISO-like 3-letter country code, e.g. MMR, THA, SGP. 
    """ 
    value = trim_upper_text(value) 
    if not value: 
        if required: 
            raise serializers.ValidationError("Country code is required.") 
        return value 
    if not re.match(r"^[A-Z]{3}$", value): 
        raise serializers.ValidationError( "Country code must be a 3-letter uppercase code, such as MMR." ) 
    return value

def validate_currency_code(value: Optional[str], required: bool = False) -> Optional[str]: 
    """ Validate ISO 3-letter currency code, e.g. MMK, USD, SGD. 
    """ 
    value = trim_upper_text(value) 
    if not value: 
        if required: 
            raise serializers.ValidationError("Currency code is required.") 
        return value 
    if not re.match(r"^[A-Z]{3}$", value): 
        raise serializers.ValidationError("Currency code must be a 3-letter uppercase code, such as MMK.") 
    return value


def validate_currency_name(value: Optional[str], required: bool = False) -> Optional[str]: 
    """ Validate Currency Name field. e.g. Myanmar Kyat, United States Dollar.
    """ 
    value = trim_text(value) 
    if not value: 
        if required: 
            raise serializers.ValidationError("Currency name is required.") 
        return value 
    return value

def validate_custodian_code(value: str) -> str:
    """ Validate Custodian Code field (e.g., EMP-001, EMP-002).
    Allows uppercase letters, numbers, hyphen, and underscore.
    """
    return validate_code_pattern(
        value=value,
        pattern=r"^[A-Z0-9\-_]+$",
        field_label="Custodian code",
    )


def validate_custodian_name(value: Optional[str], required: bool = True) -> Optional[str]:
    """ Validate Custodian Name field (e.g., U Aung Aung).
    """
    value = trim_text(value)
    if not value:
        if required:
            raise serializers.ValidationError("Custodian name is required.")
        return value
    return value