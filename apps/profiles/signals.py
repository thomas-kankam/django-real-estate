import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile
from real_estate.settings.base import AUTH_USER_MODEL

# Instance of the logger
logger = logging.getLogger(__name__)

# create a post_save signal to create a user's profile when a user is created
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
