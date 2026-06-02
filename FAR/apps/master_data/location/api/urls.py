from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.master_data.location.api.views.location_views import LocationViewSet
from apps.master_data.location.meta.location_field_meta_view import LocationFieldMetaView



router = DefaultRouter()
router.register(r'', LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls)),
    path('fields/<str:field_name>/', LocationFieldMetaView.as_view(), name='location-field-meta'),
]