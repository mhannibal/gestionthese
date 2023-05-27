from django.db import models
from user.models import User
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext as _



class SupervisorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.SUPERVISOR
            )


class Supervisor(User):
    base_type = User.Types.SUPERVISOR
    objects = SupervisorManager()

    def get_absolute_url(self):
        return reverse('detail-Supervisor', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.type=User.Types.SUPERVISOR
            self.username = f'{self.first_name}_{self.last_name}'
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        proxy = True



class SupervisorProfile(models.Model):
    user = models.OneToOneField(
        Supervisor,
        related_name='supervisor_profile',
        on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse('profile-Supervisor', kwargs={'pk': self.user.pk})

    class Meta:
        verbose_name_plural = _("Profiles de Supervisors")
        verbose_name = _("Profile de Supervisor")
