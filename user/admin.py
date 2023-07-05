from django.contrib import admin

from user.models import Balance, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_superuser', 'is_active', 'date_joined')
    list_filter = ('is_superuser', 'is_active')
    ordering = ('email', 'date_joined')
    list_per_page = 30
    search_fields = ('user', 'email')
    list_display_links = ('email',)


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    ordering = ('user', 'balance')
    list_per_page = 30
    search_fields = ('user', 'balance')
    list_display_links = ('user',)
