from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.master_data.department.api.views.department_views import DepartmentViewSet
from apps.master_data.department.meta.department_field_meta_view import DepartmentFieldMetaView  
router = DefaultRouter()
router.register(r'', DepartmentViewSet, basename='department') 
urlpatterns = [
    path('', include(router.urls)),
   path('fields/<str:field_name>/', 
         DepartmentFieldMetaView.as_view(),),
]
