from django.contrib import admin
from .models import Portfolio, LegSettings, LegExecutionDetails

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiry', 'premium_gap', 'start', 'end', 'target', 'stop_loss')
    search_fields = ('name',)
    list_filter = ('expiry',)

@admin.register(LegSettings)
class LegSettingsAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'state', 'right', 'txn', 'execution_time', 'sqoff_time', 
                    'count_sl', 'count_tp', 'wait_n_trade', 'target_premium', 'stop_loss', 
                    'take_profit', 'ProfitLockThreshold', 'LockProfitAt', 
                    'IncreaseInProfitForTrail', 'TrailProfitBy', 'SL_TrailTrigger', 
                    'SL_Trail_Amt', 'on_target', 'on_tp', 'on_sl')
    search_fields = ('portfolio__name',)
    list_filter = ('state', 'right', 'txn', 'on_target', 'on_tp', 'on_sl')

@admin.register(LegExecutionDetails)
class LegExecutionDetailsAdmin(admin.ModelAdmin):
    list_display = ('sqoff', 'execute', 'rexecute', 'rentry')
    search_fields = ('sqoff', 'execute', 'rexecute', 'rentry')