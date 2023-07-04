from datetime import datetime

from django.db import models

from user.models import User


class Transaction(models.Model):
    REPLENISHMENT = 'replenishment'
    DEBITING = 'debiting'

    TRANSACTIONS_TYPES = (
        (REPLENISHMENT, 'Пополнение'),
        (DEBITING, 'Списание')
    )

    user = models.ForeignKey(User, models.CASCADE, verbose_name='Изображение профиля', related_name='transactions')
    type = models.CharField(verbose_name='Вид транзакции', max_length=13, choices=TRANSACTIONS_TYPES)
    sum = models.PositiveIntegerField(verbose_name='Сумма')
    created_at = models.DateTimeField(verbose_name='Дата транзакции', default=datetime.now())

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return str(self.pk)
