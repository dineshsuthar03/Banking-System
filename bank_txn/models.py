

from django.db import models

class BankAccount(models.Model):
    account_holder_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number


# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = {}

#     def create_account(self, acc_holder_name, account_no, initial_balance):
#         self.accounts[account_no] = initial_balance
#         print(f"Account for {acc_holder_name} has been created")

#     def get_account_balance(self, account_number):
#         if account_number in self.accounts:
#             acc_balance = self.accounts[account_number]
#             return acc_balance
#         else:
#             return None

#     def deposit(self, account_number, amount):
#         if account_number in self.accounts:
#             self.accounts[account_number] += amount
#             print(f"Tumhara naya balance {self.accounts[account_number]}")
#         else:
#             print(f"{account_number} account not found")

#     def withdraw(self, account_number, amount):
#         if account_number in self.accounts:
#             if self.accounts[account_number] >= amount:
#                 self.accounts[account_number] -= amount
#                 print(f"Amount debited: {amount}")
#                 print(f"New balance: {self.accounts[account_number]}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Account not found.")

#     def transfer(self, from_account, to_account, amount):
#         if from_account in self.accounts and to_account in self.accounts:
#             if self.accounts[from_account] >= amount:
#                 self.accounts[from_account] -= amount
#                 self.accounts[to_account] += amount
#                 print("Transfer successful.")
#             else:
#                 print("Insufficient balance for transfer.")
#         else:
#             print("Account(s) not found.")




from .models import BankAccount

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def create_account(self, acc_holder_name, account_no, initial_balance):
        account, created = BankAccount.objects.get_or_create(
            account_number=account_no,
            defaults={'account_holder_name': acc_holder_name, 'balance': initial_balance}
        )
        if created:
            print(f"Account for {acc_holder_name} has been created at {self.bank_name}")

    def get_account_balance(self, account_number):
        try:
            account = BankAccount.objects.get(account_number=account_number)
            return account.balance
        except BankAccount.DoesNotExist:
            return None

    def deposit(self, account_number, amount):
        try:
            account = BankAccount.objects.get(account_number=account_number)
            account.balance += amount
            account.save()
            print(f"Tumhara naya balance {account.balance}")
        except BankAccount.DoesNotExist:
            print(f"{account_number} account not found")

    def withdraw(self, account_number, amount):
        try:
            account = BankAccount.objects.get(account_number=account_number)
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                print(f"Amount debited: {amount}")
                print(f"New balance: {account.balance}")
            else:
                print("Insufficient balance.")
        except BankAccount.DoesNotExist:
            print("Account not found.")

    def transfer(self, from_account, to_account, amount):
        try:
            sender_account = BankAccount.objects.get(account_number=from_account)
            receiver_account = BankAccount.objects.get(account_number=to_account)

            if sender_account.balance >= amount:
                sender_account.balance -= amount
                receiver_account.balance += amount
                sender_account.save()
                receiver_account.save()
                print(f"Transfer successful from {self.bank_name}")
            else:
                print("Insufficient balance for transfer.")
        except BankAccount.DoesNotExist:
            print("Account(s) not found.")
