from django.db import models
from django.contrib.auth.models import BaseUserManager


class StaffManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        create staff with email and password
        """
        if not email:
            raise ValueError('Staff must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.can_login = True
        user.save(using=self._db)
        return user