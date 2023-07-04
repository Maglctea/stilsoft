from django.contrib import admin

from user.models import Balance, User


@admin.register(User)
class HostedAppAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser', 'is_active', 'date_joined')
    list_filter = ('is_superuser', 'is_active')
    ordering = ('username', 'email', 'date_joined')
    list_per_page = 30
    search_fields = ('user', 'email')
    list_display_links = ('username', 'email')


@admin.register(Balance)
class HostedAppAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    ordering = ('user', 'balance')
    list_per_page = 30
    search_fields = ('user', 'balance')
    list_display_links = ('user',)
