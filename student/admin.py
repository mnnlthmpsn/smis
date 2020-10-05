from django.contrib import admin
from .models import Student, HealthReport

# Register your models here.
admin.site.register(Student)
admin.site.register(HealthReport)