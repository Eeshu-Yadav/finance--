from rest_framework import serializers
from .models import Portfolio, LegSettings, LegExecutionDetails,RequestData

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



class ExecuteFunctionSerializer(serializers.Serializer):
    option = serializers.CharField()
    legs = serializers.ListField(child=serializers.CharField(), required=False)
    oppo_leg = serializers.CharField(required=False)

class RequestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestData
        fields = '__all__'
