from django.urls import path, include
from .views import ApiRootView

urlpatterns = [

    path('', ApiRootView.as_view(), name='api-root'),
    
    path('branches/', include('apps.master_data.branch.api.urls')),
    path('countries/', include('apps.master_data.country.api.urls')),
    path('currencies/', include('apps.master_data.currency.api.urls')),
    path('locations/', include('apps.master_data.location.api.urls')),
    path('departments/', include('apps.master_data.department.api.urls')),
    path('custodians/', include('apps.master_data.custodian.api.urls')),
]