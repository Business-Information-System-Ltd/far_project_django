from rest_framework.views import APIView
from rest_framework.response import Response


from apps.master_data.currency.meta.currency_meta import CurrencyFieldMeta




class CurrencyFieldMetaView(APIView):

    def get(self, request, field_name):
        meta = CurrencyFieldMeta.get_field_meta(field_name)

        if not meta:
            return Response({"error": "Field not found"}, status=404)

        return Response({
            "field": field_name,
            "meta": meta
        })


