from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.master_data.country.api.views.country_views import CountryViewSet
from apps.master_data.country.models.country_models import Country



router = DefaultRouter()
router.register(r'', CountryViewSet)

urlpatterns = [
     path('', include(router.urls)),
    

]
