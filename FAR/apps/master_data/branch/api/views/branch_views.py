
from django.shortcuts import render
from rest_framework import viewsets

from apps.master_data.branch.models.branch_models import Branch
from apps.master_data.branch.api.serializers.branch_serializers import BranchSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

