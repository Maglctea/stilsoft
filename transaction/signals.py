from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver

from transaction import models
from transaction.models import Transaction
from user.models import Balance


@receiver(pre_save, sender=models.Transaction)
def post_save_transaction(**kwargs):
    new_transaction = kwargs.get('instance')
    modifier = 1 if new_transaction.type == Transaction.DEBITING else -1

    if Transaction.objects.filter(pk=new_transaction.pk).exists():
        old_transaction = Transaction.objects.get(pk=new_transaction.pk)
        old_modifier = 1 if old_transaction.type == Transaction.REPLENISHMENT else -1
        balance_difference = old_modifier * old_transaction.sum + modifier * new_transaction.sum
    else:
        balance_difference = modifier * new_transaction.sum

    Balance.objects.filter(user=new_transaction.user).update(balance=F('balance') - balance_difference)
