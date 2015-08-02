from django.contrib import admin
from django.contrib.messages import constants as messages
from home.models import Theme

# Color codes used to pick a theme
COLOR_CODES = {
    "Blue": "#337ab7",
    "Green": "#5cb85c",
    "Yellow": "#f0ad4e",
    "Light Blue": "#5bc0de",
    "Red": "#d9534f"
}


class ThemeAdmin(admin.ModelAdmin):
    """
    Admin look and feel for the theme, home and search page of the website.
    User enter pictures as well as a color to change the websites look and feel
    Affects only the home page, search page and the background colors
    """
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

    # How to display all header entries in the admin list
    list_display = ('pub_date', 'theme_name', 'current_theme')

    # Users can filter the list from the published date or the theme name
    list_filter = ('pub_date', 'theme_name')

    actions = ["make_current_theme"]

    # Action that enables a selected theme as the main theme. (Note only one theme is allowed for this action)
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

    # Before saving the model, change the theme color code to match the users choice
    def save_model(self, request, obj, form, change):
        if Theme.objects.count() == 0:
            obj.current_theme = True
        obj.menu_background = COLOR_CODES[obj.get_theme_choice_display()]
        obj.save()


admin.site.register(Theme, ThemeAdmin)