from django.db import models

# Create your models here.
class Clss(models.Model):
    name = models.CharField(max_length=10, default='Class 1')
    fee = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name