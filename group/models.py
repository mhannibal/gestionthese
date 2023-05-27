from django.db import models
from supervisor.models import Supervisor


class Subject(models.Model):
  supervisor = models.ForeignKey(
    Supervisor,
    related_name='subject',
    on_delete=models.CASCADE)
  title = models.CharField(max_length=100, blank=False)
  description = models.TextField(blank=True)
  is_confirmed = models.BooleanField(default=False)


class Group(models.Model):
  name = models.CharField(max_length=100, blank=False)
  subject = models.OneToOneField(
    Subject,
    null=True,
    on_delete=models.SET_NULL)
  is_confirmed = models.BooleanField(default=False)
  results = models.CharField(max_length=10, blank=True)