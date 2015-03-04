from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import Writer

class WriteInLine(admin.StackedInline):
    model = Writer
    can_delete = False
    verbose_name_plural = "writer"


class UserAdmin(UserAdmin):
    inlines = [WriteInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

