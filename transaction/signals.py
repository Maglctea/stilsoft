from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from transaction import models
from user.models import Balance


@receiver(post_save, sender=models.Transaction)
def post_save_transaction(created, **kwargs):
    if created:
        transaction = kwargs.get('instance')

        modifier = 1
        if transaction.transaction_type == 'debiting':
            modifier = -1

        Balance.objects.filter(user=transaction.user).update(balance=F('balance') + modifier * transaction.sum)
