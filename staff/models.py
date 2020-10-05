from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import StaffManager

# Create your models here.
class Staff(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address', unique=True, max_length=255)
    name = models.CharField(verbose_name='Staff Fullname', max_length=300)
    is_active = models.BooleanField(default=True)
    can_login = models.BooleanField(default=False)

    objects = StaffManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.can_login