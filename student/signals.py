from .models import Student, StudentProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from group.models import Group


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created :
      StudentProfile.objects.create(user=instance)
      


@receiver(post_save, sender=StudentProfile)
def create_group_assign_toLeader(sender, instance, created, **kwargs):
    print(instance)    
    print(sender)
    if  instance.is_group_leader and instance.group == None:
        group = Group.objects.create(name=f'group {Group.objects.count() + 1}')
        instance.group = group
        instance.save()

      

