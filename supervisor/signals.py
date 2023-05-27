from django.db import models
from .models import Supervisor, SupervisorProfile
from user.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Supervisor)
def create_student_profile(sender, instance, created, **kwargs):
    if created :
        SupervisorProfile.objects.create(user=instance)
