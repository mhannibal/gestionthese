from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"
        SUPERVISOR = "SUPERVISOR", "Supervisor"
        STUDENT = "STUDENT", "Student"
    base_type = Types.STUDENT

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, )
    last_name = models.CharField(max_length=150,)
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    type = models.CharField(
        _("Type"), max_length=50,
        choices=Types.choices,
        default=Types.STUDENT
    )

    
    address = models.CharField(_('address'), max_length=200, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.email}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.type
        return super().save(*args, **kwargs)