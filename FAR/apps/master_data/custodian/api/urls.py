# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from apps.master_data.custodian.models.custodian_models import Custodian
# from apps.master_data.custodian.api.views.custodian_views import CustodianViewSet
# from .serializers import *
# router = DefaultRouter()
# router.register(r'',CustodianViewSet)


# urlpatterns = [
#     path('',include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.master_data.custodian.api.views.custodian_views import CustodianViewSet
from apps.master_data.custodian.meta.custodian_field_meta_view import CustodianFieldMetaView

router = DefaultRouter()
router.register(r'', CustodianViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "fields/<str:field_name>/",
        CustodianFieldMetaView.as_view()
    ),
]
