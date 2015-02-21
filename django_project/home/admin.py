from django.contrib import admin
from django.contrib.messages import constants as messages
from home.models import Header

COLOR_CODES = {
    "Blue": "#337ab7",
    "Green": "#5cb85c",
    "Yellow": "#f0ad4e",
    "Light Blue": "#5bc0de",
    "Red": "#d9534f"
}


class HeaderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Theme", {
            "fields": ["theme_name", "header_cover", "footer_cover", "theme_choice"],
        }),
        ("Header", {
            "fields": ["main_heading", "sub_heading"]
        }),
        ("Body", {
            "fields": ["title_text", "summary_text"]
        }),
    ]

    change_form_template = "home/admin/change_form.html"

    list_display = ('pub_date', 'theme_name', 'current_header')

    list_filter = ('pub_date', 'theme_name')

    actions = ["make_current_header"]

    def make_current_header(self, request, queryset):
        if len(queryset) == 1:
            Header.objects.update(current_header=False)
            queryset.update(current_header=True)
        else:
            self.message_user(request,
                              "ERROR: you can only select one header for this action, you've selected %s" % len(
                                  queryset),
                              level=messages.ERROR)

    make_current_header.short_description = "Set as Current Header"

    def save_model(self, request, obj, form, change):
        if Header.objects.count() == 0:
            obj.current_header = True
        obj.menu_background = COLOR_CODES[obj.get_theme_choice_display()]
        obj.save()


admin.site.register(Header, HeaderAdmin)