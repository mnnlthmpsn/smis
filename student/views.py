from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import Student
from .helpers import create_account as createAccount, create_transaction 
from .forms import StudentForm
from clss.models import Clss
from staff.models import Staff
from account.models import Account
from smis.helpers import all_items
from decimal import Decimal
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    all_students = all_items(Student)
    return render(request, 'student/index.html', {'students': all_students})

@login_required
def pay_fees(request, student_id):
    student = Student.objects.get(id=student_id)
    acc = Account.objects.get(student=student_id)
    if request.method == 'POST':
        amt = Decimal(request.POST['amount'])
        acc.amount -= amt
        if acc.amount < 0:
            messages.add_message(request, messages.INFO, 'Error!!! Cannot pay more than owed')
        else:
            acc.save()
            transaction = create_transaction(acc, amt, 'School Fees')
        return HttpResponseRedirect(reverse('account:index', kwargs={'student_id': student_id}))
    return render(request, 'student/pay_fees.html', {'student': student})

@login_required
def enroll(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            other_names = form.cleaned_data['other_names']
            date_of_birth = form.cleaned_data['date_of_birth']
            form.save()
            student = Student.objects.get(firstname=firstname,lastname=lastname,other_names=other_names,date_of_birth=date_of_birth)
            account = Account.objects.get(student=student)
            account.amount += student.clss.fee
            account.save()
            return HttpResponseRedirect(reverse('student:index'))
    return render(request, 'student/enroll.html', {
        'form': form
    })


@login_required
def update(request, student_id):
    student = Student.objects.get(pk=student_id)
    old_class = student.clss
    form = StudentForm(instance=student)
    if request.method == 'POST':
        if form.is_valid:
            form = StudentForm(request.POST, request.FILES, instance=student)
            form.save()

            # compare new and old class
            # if class changes, update account, else update only

            new_class = Clss.objects.get(id=request.POST['clss'])

            if old_class == new_class:
               pass
            else:
                account = Account.objects.get(student=student.id)
                account.amount = 0
                account.amount += new_class.fee
                print(new_class.fee)
                account.save()
            return HttpResponseRedirect(reverse('student:index'))
    return render(request, 'student/update.html', {'form': form})


@login_required
def delete_student(request, student_id):
    std = Student.objects.get(pk=student_id).delete()
    return HttpResponseRedirect(reverse('student:index'))
@login_required
def std_account(request, student_id):
    pass