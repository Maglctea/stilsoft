from django.db.models.signals import post_save
from django.dispatch import receiver

import stilsoft.settings
from user.models import Balance


@receiver(post_save, sender=stilsoft.settings.AUTH_USER_MODEL)
def post_save_user(created, **kwargs):
    """Signal to create a user balance when creating a user"""

    if created:
        user = kwargs.get('instance')
        Balance.objects.create(user=user, balance=0)