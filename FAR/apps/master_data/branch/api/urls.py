from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.master_data.branch.api.views.branch_views import BranchViewSet
from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.branch.meta.branch_field_meta_view import BranchFieldMetaView


router = DefaultRouter()
router.register(r'', BranchViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path(
        "meta/fields/<str:field_name>/",
        BranchFieldMetaView.as_view()
    ),

]
