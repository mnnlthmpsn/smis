from django.db import models
from student.models import Student

# Create your models here.
class Account(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return f'{self.student.get_full_name()}'

class Transactions(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.account.student.get_full_name()