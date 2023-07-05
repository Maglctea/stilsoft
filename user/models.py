from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.manager import UserManager


class User(AbstractUser):
    objects = UserManager()
    password = models.CharField(_("password"), max_length=128, blank=False)
    email = models.EmailField(_('email address'), unique=True)

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password',)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Balance(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='balance')
    balance = models.IntegerField('Баланс', default=0)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'

    def __str__(self):
        return f'{self.user.username} - {self.balance}'
