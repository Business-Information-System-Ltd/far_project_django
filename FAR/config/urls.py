"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include
from apps.master_data.currency.meta.currency_field_meta_view import CurrencyFieldMetaView
from apps.master_data.custodian.meta.custodian_field_meta_view import CustodianFieldMetaView

from rest_framework.routers import DefaultRouter

from apps.master_data.branch.meta.branch_field_meta_view import BranchFieldMetaView
urlpatterns = [
    path('admin/', admin.site.urls),

    # path('api/far/meta/currencies/fields/',
    #      CurrencyFieldMetaView.as_view()),

    # path('api/far/meta/currencies/fields/',
    #      CustodianFieldMetaView.as_view()),

    path('api/far/meta/', include([
        path('branches/', include('apps.master_data.branch.api.urls')),
        path('countries/', include('apps.master_data.country.api.urls')),
        path('currencies/', include('apps.master_data.currency.api.urls')),
        path('locations/', include('apps.master_data.location.api.urls')),
        path('departments/', include('apps.master_data.department.api.urls')),
        path('custodians/', include('apps.master_data.custodian.api.urls')),
        path('currencies/fields', include('apps.master_data.currency.api.urls')),
        path('custodians/fields', include('apps.master_data.custodian.api.urls')),


        

    ])),
]
