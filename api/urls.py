from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, LegSettingsViewSet, LegExecutionDetailsViewSet, execute_on_tp, execute_on_sl, get_tp_options, get_sl_options

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'legsettings', LegSettingsViewSet)
router.register(r'legexecutiondetails', LegExecutionDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('execute_on_tp/', execute_on_tp, name='execute_on_tp'),
    path('execute_on_sl/', execute_on_sl, name='execute_on_sl'),
    path('get_tp_options/', get_tp_options, name='get_tp_options'),
    path('get_sl_options/', get_sl_options, name='get_sl_options'),
]
