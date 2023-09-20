from django.shortcuts import render
from django.http import JsonResponse
import yfinance as yf
from rest_framework import serializers
from backtesting.models import indicator, SMA, entry_condition, Strategy, Parameter
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def backtest_view(request):
    print("Before Post")
    if request.method == 'POST':
        print("Entered Post")
        json_data = json.loads(request.body)
        print(json_data)
        name = json_data['name']
        print(name)
        condition = json_data['entry_condition']
        print(condition)
        indicator_name = condition['indicator_1']['name']
        print(indicator_name)
        indicator_window = condition['indicator_1']['window']
        print(indicator_window)
        sma_instance = SMA.objects.create(name=indicator_name, window=indicator_window)
        print(sma_instance)
        entry_condition_instance = entry_condition.objects.create(indicator_1 = sma_instance)
        print(entry_condition_instance)
        strategy_instance = Strategy.objects.create(name=name, condition=entry_condition_instance)
        print(strategy_instance)
        parameter_instance = Parameter.objects.create(window=indicator_window)
        print(parameter_instance)

    return JsonResponse({"message": "Backtest completed successfully"})

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})



