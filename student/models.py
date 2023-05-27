from django.db import models
from user.models import User
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse
from django.utils.translation import gettext as _
from group.models import Group

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
                type=User.Types.STUDENT
            )

class Student(User):
    base_type = User.Types.STUDENT
    objects = StudentManager()
    
    def get_absolute_url(self):
        return reverse('detail-Student', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.username = f'{self.first_name}_{self.last_name}'
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        proxy = True


class StudentProfile(models.Model):
    user = models.OneToOneField(
        Student,
        related_name='student_profile', 
        on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)
    is_group_leader = models.BooleanField(default=False)
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} group leader:{self.is_group_leader}'

    def get_absolute_url(self): 
        return reverse('profile-Student', kwargs={'pk': self.user.pk})

    class Meta:
        verbose_name_plural = _("Profiles de Students")
        verbose_name = _("Profile de Student")
