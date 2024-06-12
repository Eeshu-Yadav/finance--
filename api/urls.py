from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, LegSettingsViewSet, LegExecutionDetailsViewSet

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'legsettings', LegSettingsViewSet)
router.register(r'legexecutiondetails', LegExecutionDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]