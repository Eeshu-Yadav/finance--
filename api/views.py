from rest_framework import viewsets
from .models import Portfolio, LegSettings, LegExecutionDetails
from .serializers import PortfolioSerializer, LegSettingsSerializer, LegExecutionDetailsSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class LegSettingsViewSet(viewsets.ModelViewSet):
    queryset = LegSettings.objects.all()
    serializer_class = LegSettingsSerializer

class LegExecutionDetailsViewSet(viewsets.ModelViewSet):
    queryset = LegExecutionDetails.objects.all()
    serializer_class = LegExecutionDetailsSerializer