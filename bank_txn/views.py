# from django.shortcuts import render

# # Create your views here.

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")


from django.shortcuts import render
from django.http import HttpResponse
from .models import Bank

# Create an instance of the Bank class
bank = Bank("MyBank")

def home(request):
    return render(request, 'bank_txn/home.html')

def create_account(request):
    if request.method == 'POST':
        acc_holder_name = request.POST['acc_holder_name']
        account_no = request.POST['account_no']
        initial_balance = float(request.POST['initial_balance'])
        bank.create_account(acc_holder_name, account_no, initial_balance)
    return render(request, 'bank_txn/create_account.html')

def get_account_balance(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        account_balance = bank.get_account_balance(account_number)
        return HttpResponse(f"Balance for {account_number} is {account_balance}")
    return render(request, 'bank_txn/get_account_balance.html')

# Implement other views: deposit, withdraw, transfer
# ...


# ...

def deposit(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        amount = float(request.POST['amount'])
        bank.deposit(account_number, amount)
    return render(request, 'bank_txn/deposit.html')

def withdraw(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        amount = float(request.POST['amount'])
        bank.withdraw(account_number, amount)
    return render(request, 'bank_txn/withdraw.html')

def transfer(request):
    if request.method == 'POST':
        from_account = request.POST['from_account']
        to_account = request.POST['to_account']
        amount = float(request.POST['amount'])
        bank.transfer(from_account, to_account, amount)
    return render(request, 'bank_txn/transfer.html')

# ...



