from account.models import Account
from .models import Student
from account.models import Transactions

def create_account(std):
    acc = Account(student=std, amount=0)
    acc.save()
    return True

def create_transaction(acc, amount, desc):
    trns = Transactions(account=acc, amount=amount, description=desc)
    trns.save()
    return trns