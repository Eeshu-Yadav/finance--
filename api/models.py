# myapp/models.py

from django.db import models
from functools import partial

class Portfolio(models.Model):
    EXPIRY_CHOICES = (
        ('daily_exp', 'Daily Expiry'),
        ('weekly_exp', 'Weekly Expiry'),
        ('monthly_exp', 'Monthly Expiry'),
    )
    name = models.CharField(max_length=255)
    expiry = models.CharField(max_length=50, choices=EXPIRY_CHOICES)
    premium_gap = models.TextField(null=True, blank=True)
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    target = models.FloatField()
    stop_loss = models.FloatField(null=True, blank=True)

class LegSettings(models.Model):
    STATE_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    RIGHT_CHOICES = (
        ('C', 'Call'),
        ('P', 'Put'),
    )
    TXN_CHOICES = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    )
    ON_TARGET = (
        ('none', 'None'),
        ('leg', 'Leg'),
        ('current_portfolio', 'Current Portfolio'),
        ('other_portfolio', 'Other Portfolio'),
    )
    ON_TP_CHOICES = (
        ('ReExecuteLeg', 'ReExecuteLeg'),
        ('ReEnterLeg', 'ReEnterLeg'),
        ('KeepLegRunning', 'KeepLegRunning'),
        #('Execute_Legs', 'Execute_Legs'),
        ('partial', 'partial'),
    )
    ON_SL_CHOICES = (
        ('ReExecuteLeg', 'ReExecuteLeg'),
        ('ReEnterLeg', 'ReEnterLeg'),
        ('KeepLegRunning', 'KeepLegRunning'),
        ('partial', 'partial'),
        
        # ('ReExecute_At_Opposite_Leg_Ltp', 'ReExecute_At_Opposite_Leg_Ltp'),
        # ('SqOff_Legs', 'SqOff_Legs'),
        # ('Execute_Legs', 'Execute_Legs'),
    )

    portfolio = models.ForeignKey(Portfolio, related_name='leg_settings', on_delete=models.CASCADE)
    state = models.IntegerField(choices=STATE_CHOICES)
    right = models.CharField(max_length=1, choices=RIGHT_CHOICES)
    txn = models.CharField(max_length=4, choices=TXN_CHOICES)
    execution_time = models.TimeField(null=True, blank=True)
    sqoff_time = models.TimeField(null=True, blank=True)
    count_sl = models.PositiveIntegerField()
    count_tp = models.PositiveIntegerField()
    wait_n_trade = models.TextField(null=True, blank=True)
    target_premium = models.FloatField()
    stop_loss = models.FloatField(null=True, blank=True)
    take_profit = models.FloatField(null=True, blank=True)
    ProfitLockThreshold = models.FloatField(null=True, blank=True)
    LockProfitAt = models.FloatField(null=True, blank=True)
    IncreaseInProfitForTrail = models.FloatField(null=True, blank=True)
    TrailProfitBy = models.FloatField(null=True, blank=True)
    SL_TrailTrigger = models.TextField(null=True, blank=True)
    SL_Trail_Amt = models.TextField(null=True, blank=True)
    on_target = models.CharField(max_length=20, choices=ON_TARGET)
    on_tp = models.CharField(max_length=50, choices=ON_TP_CHOICES, null=True, blank=True)
    on_sl = models.CharField(max_length=50, choices=ON_SL_CHOICES, null=True, blank=True)

class LegExecutionDetails(models.Model):
    sqoff = models.TimeField()
    execute = models.TimeField()
    rexecute = models.TimeField()
    rentry = models.TimeField()
