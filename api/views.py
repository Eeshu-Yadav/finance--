from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExecuteFunctionSerializer, RequestDataSerializer
from .utils import ON_TP_FUNCTIONS, ON_SL_FUNCTIONS
from rest_framework import viewsets
from .models import Portfolio, LegSettings, LegExecutionDetails, RequestData
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

@api_view(['POST'])
def execute_on_tp(request):
    save_request_data(request, 'execute_on_tp')
    serializer = ExecuteFunctionSerializer(data=request.data)
    if serializer.is_valid():
        option = serializer.validated_data['option']
        
        if option in ON_TP_FUNCTIONS:
            function_or_partial = ON_TP_FUNCTIONS.get(option)
            if callable(function_or_partial):
                if 'partial_execute_legs' in option:
                    legs = serializer.validated_data.get('legs', [])
                    function_or_partial.keywords['legs'] = legs
                function_or_partial()
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error', 'message': f'{option} is not callable'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'error', 'message': f'{option} is not a valid option'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def execute_on_sl(request):
    save_request_data(request, 'execute_on_sl')
    serializer = ExecuteFunctionSerializer(data=request.data)
    if serializer.is_valid():
        option = serializer.validated_data['option']
        
        if option in ON_SL_FUNCTIONS:
            function_or_partial = ON_SL_FUNCTIONS.get(option)
            if callable(function_or_partial):
                if 'partial_sqoff_legs' in option:
                    legs = serializer.validated_data.get('legs', [])
                    function_or_partial.keywords['legs'] = legs
                elif 'partial_reexecute_opposite_leg' in option:
                    oppo_leg = serializer.validated_data.get('oppo_leg', '')
                    function_or_partial.keywords['oppo_leg'] = oppo_leg
                
                function_or_partial()
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error', 'message': f'{option} is not callable'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'error', 'message': f'{option} is not a valid option'}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tp_options(request):
    data = RequestData.objects.filter(endpoint='execute_on_tp')
    serializer = RequestDataSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_sl_options(request):
    data = RequestData.objects.filter(endpoint='execute_on_sl')
    serializer = RequestDataSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def save_request_data(request, endpoint):
    RequestData.objects.create(
        endpoint=endpoint,
        data=request.data
    )
