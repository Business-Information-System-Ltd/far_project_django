import re
from typing import Optional
from rest_framework import serializers

def trim_upper_text(value: Optional[str]) -> Optional[str]:
    """
    Trims whitespace and converts string to uppercase.
    """
    if value is None:
        return None
    return str(value).strip().upper()

def uppercase_text(value: Optional[str]) -> Optional[str]:
    """
    Converts string to uppercase.
    """
    if value is None:
        return None
    return str(value).upper()

def validate_country_code(value: Optional[str], required: bool = False) -> Optional[str]: 
    """ 
    Validate ISO-like 3-letter country code, e.g. MMR, THA, SGP. 
    """ 
    value = trim_upper_text(value) 
    
    if not value: 
        if required: 
            raise serializers.ValidationError("Country code is required.") 
        return value 
    
    if not re.match(r"^[A-Z]{3}$", value): 
        raise serializers.ValidationError("Country code must be a 3-letter uppercase code, such as MMR.") 
        
    return value