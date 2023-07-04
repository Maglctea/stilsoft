from django.contrib import admin

from user.models import Balance, User

admin.site.register(User)
admin.site.register(Balance)
