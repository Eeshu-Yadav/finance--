from rest_framework import serializers
from .models import Portfolio, LegSettings, LegExecutionDetails

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class LegSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegSettings
        fields = '__all__'

class LegExecutionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegExecutionDetails
        fields = '__all__'