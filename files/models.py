from django.db import models
from group.models import Group

class File(models.Model):
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE
    )
    name= models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    is_confirmed = models.BooleanField(default=False)

