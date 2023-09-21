from django.db import models
from enum import Enum
# from django.contrib.postgres.fields import JSONField
# Create your models here.

# class BacktestParameters(models.Model):
#     start_date = models.DateField()
#     end_date = models.DateField()
#     ticker_symbol = models.CharField(max_length=10)




class Parameter(models.Model):
    window = models.IntegerField()
    weights = models.IntegerField(default=0)
    fast_period = models.IntegerField(default=0)
    slow_period = models.IntegerField(default=0)


class indicator(models.Model):
    name = models.CharField(max_length=10)
    # parameter = models.ForeignKey(Parameter, on_delete=models.PROTECT, null=True)
    # parameter = models.JSONField()

class SMA(indicator):
    window = models.IntegerField()

class entry_condition(models.Model):
    indicator_1 = models.ForeignKey(indicator, on_delete=models.PROTECT, null=True)

class Strategy(models.Model):
    name = models.CharField(max_length=10)
    condition = models.ForeignKey(entry_condition, on_delete=models.PROTECT, null=True)

class name_map(Enum):
    sma = SMA





