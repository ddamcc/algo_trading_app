from django.urls import path
from . import views

urlpatterns = [
    path('backtest/', views.backtest_view, name='backtest'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token')
]