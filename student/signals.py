from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, HealthReport
from account.models import Account

@receiver(post_save, sender=Student)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(student=instance)
        HealthReport.objects.create(student=instance)

@receiver(post_save, sender=Student)
def save_account(sender, instance, **kwargs):
    instance.account.save()
    instance.healthreport.save()