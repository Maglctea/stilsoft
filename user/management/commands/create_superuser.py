import os

from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):
    """Create superuser"""
    def handle(self, *args, **options):
        User.objects.create_superuser(password='admin', email='admin@admin.ru')