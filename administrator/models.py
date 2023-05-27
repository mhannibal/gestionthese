from django.db import models
from user.models import User
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext as _



class AdministratorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.ADMINISTRATOR
            )


class Administrator(User):
    base_type = User.Types.ADMINISTRATOR
    objects = AdministratorManager()

    def get_absolute_url(self):
        return reverse('detail-Administrator', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.username = f'{self.first_name}_{self.last_name}'
            self.type=User.Types.ADMINISTRATOR
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        proxy = True



class AdministratorProfile(models.Model):
    user = models.OneToOneField(
        Administrator,
        related_name='profile',
        on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse('profile-Administrator', kwargs={'pk': self.user.pk})

    class Meta:
        verbose_name_plural = _("Profiles de Administrators")
        verbose_name = _("Profile de Administrator")
