from rest_framework.views import APIView
from rest_framework.response import Response
# Assuming CountryFieldMeta is in the same file as you shared, 
# if it's in a different file, import it accordingly.

class CountryFieldMeta:
    _meta_data = {
        "country_code": {
            "label": "Country Code",
            "type": "string",
            "max_length": 3,
            "help_text": "Enter the 3-letter ISO country code (e.g., MMR)."
        },
        "country_name": {
            "label": "Country Name",
            "type": "string",
            "max_length": 100,
            "help_text": "Enter the full name of the country."
        }
    }

    @classmethod
    def get_field_meta(cls, field_name):
        return cls._meta_data.get(field_name)

# --- ADD THIS PART TO YOUR FILE ---
class CountryFieldMetaView(APIView):
    def get(self, request, field_name):
        meta = CountryFieldMeta.get_field_meta(field_name)

        if not meta:
            return Response({"error": "Field not found"}, status=404)

        return Response({
            "field": field_name,
            "meta": meta
        })