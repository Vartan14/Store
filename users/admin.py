from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'created_at', 'expires_at')
    fields = ('code', 'user', 'created_at', 'expires_at')
    readonly_fields = ('created_at',)
