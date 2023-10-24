from django.urls import path
from . import views

app_name = 'bank_txn'

urlpatterns = [
    path('', views.home, name='home'),
    path('create-account/', views.create_account, name='create_account'),
    path('get-account-balance/', views.get_account_balance, name='get_account_balance'),
    # Add URLs for other views: deposit, withdraw, transfer
    # ...
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transfer/', views.transfer, name='transfer'),
]
