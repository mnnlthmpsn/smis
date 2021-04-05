from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Account, Transactions

from num2words import num2words


@login_required
def index(request, student_id):
    account = Account.objects.get(student=student_id)
    return render(request, 'account/index.html', {'account': account})

@login_required
def get_transactions(request, account_id):
    acc = Account.objects.get(id=account_id)
    all_transactions = acc.transactions_set.all()
    return render(request, 'account/transactions.html', {'transactions': all_transactions})


def render_pdf_view(request, pk):
    transaction = get_object_or_404(Transactions, pk=pk)
    wd = num2words(transaction.amount)
    return render(request, 'receipt/index.html', {'transaction': transaction, 'wd': wd})
 