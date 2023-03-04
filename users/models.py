from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # firstName = models.CharField(max_length=255, blank=False, null=False)
    # lastName = models.CharField(max_length=255, blank=False, null=False)
    # username = models.CharField(max_length=255, blank=False, null=False)
    # email = models.EmailField(blank=False, null=False)
    weight = models.IntegerField()
    DOB = models.DateTimeField(blank=False, null=False)
    age = models.IntegerField()

# @receiver(models.signals.post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance, firstName=instance.first_name, lastName=instance.last_name, email=instance.email)