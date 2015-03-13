from django.contrib import admin
from django.contrib.messages import constants as messages
from home.models import Theme

COLOR_CODES = {
    "Blue": "#337ab7",
    "Green": "#5cb85c",
    "Yellow": "#f0ad4e",
    "Light Blue": "#5bc0de",
    "Red": "#d9534f"
}


class ThemeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Theme", {
            "fields": ["theme_name", "theme_choice"],
        }),
        ("Home", {
            "fields": ["home_header_cover", "home_footer_cover"]
        }),
        ("Search", {
            "fields": ["search_header_cover", "search_footer_cover"]
        }),
    ]

    list_display = ('pub_date', 'theme_name', 'current_theme')

    list_filter = ('pub_date', 'theme_name')

    actions = ["make_current_theme"]

    def make_current_theme(self, request, queryset):
        if len(queryset) == 1:
            Theme.objects.update(current_theme=False)
            queryset.update(current_theme=True)
        else:
            self.message_user(request,
                              "ERROR: you can only select one theme for this action, you've selected %s" % len(
                                  queryset),
                              level=messages.ERROR)

    make_current_theme.short_description = "Set as Current Theme"

    def save_model(self, request, obj, form, change):
        if Theme.objects.count() == 0:
            obj.current_theme = True
        obj.menu_background = COLOR_CODES[obj.get_theme_choice_display()]
        obj.save()


admin.site.register(Theme, ThemeAdmin)