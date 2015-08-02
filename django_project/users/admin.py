from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import Writer


class WriteInLine(admin.StackedInline):
    """
    Settings for the inline object, each user must
    have the entire user model filled
    """
    model = Writer
    can_delete = False
    verbose_name_plural = "writer"


class UserAdmin(UserAdmin):
    inlines = [WriteInLine]

# remove the user admin page and add our new page with the inline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)