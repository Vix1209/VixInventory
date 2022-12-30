from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender = User)
def creatUserProfile(sender, instance, created, **kwargs):
    print('Sender --> ', sender)
    print('Instance --> ', instance)
    print('Created --> ', created)
    if created :
        Profile.objects.create(staff=instance)