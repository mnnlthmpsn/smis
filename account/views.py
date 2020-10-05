from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Account, Transactions
from student.models import Student

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

@login_required
def index(request, student_id):
    account = Account.objects.get(student=student_id)
    return render(request, 'account/index.html', {'account': account})

@login_required
def get_transactions(request, account_id):
    acc = Account.objects.get(id=account_id)
    all_transactions = acc.transactions_set.all()
    return render(request, 'account/transactions.html', {'transactions': all_transactions})

@login_required
def generate_pdf(request, transaction_id):

    transaction = Transactions.objects.get(id=transaction_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inlne: filename={transaction.account}.pdf'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    # create pdf
    p.setFont('Helvetica', 10, leading=None)
    p.drawString(220, 800, 'Halifax Maple Montessori School')
    p.drawString(220, 780, '(Creche, Nursery, Kindergaten)')
    p.line(0, 760, 1000, 760)
    p.line(0, 758, 1000, 758)
    x1 = 20
    y1 = 750
    stars = '-' * 100
    p.drawString(x1, y1-20, f'Account : {transaction.account} ')
    p.drawString(x1 + 45, y1-25, stars)
    p.drawString(x1, y1-50, f'Amount Paid : GHc: {transaction.amount} only')
    p.drawString(x1 + 65, y1-55, stars)
    p.drawString(x1, y1-80, f'Payment Type : {transaction.description}')
    p.drawString(x1 + 72, y1-85, stars)
    p.drawString(x1, y1-110, f'Payment Date : {transaction.date.date()}')
    p.drawString(x1 + 72, y1-115, stars)

    # staff name and signature
    staff_line = '-' * 50
    p.drawString(x1, y1-180, f'sign: {staff_line}') 
    p.drawString(x1, y1-200, 'Staff:')
    # Guardian name and signature
    p.drawString(x1 + 350, y1-180, f'sign: {staff_line}')
    p.drawString(x1 + 350, y1-200, 'Guardian:')
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response