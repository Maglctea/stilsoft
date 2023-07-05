from django.contrib import admin

from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'type', 'sum', 'created_at')
    list_filter = ('type',)
    ordering = ('user', 'pk', 'created_at')
    list_per_page = 30
    search_fields = ('user', 'sum')
    list_display_links = ('user',)