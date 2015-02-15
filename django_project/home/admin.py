from django.contrib import admin
from django.contrib.messages import constants as messages
from home.models import Header


class HeaderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {
            "fields": ["main_heading", "sub_heading", "button_text"]
        }),
        ("Body", {
            "fields": ["title_text", "summary_text"]
        }),
    ]

    list_display = ('pub_date', 'sub_heading', 'current_header')

    list_filter = ('pub_date', 'current_header')

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
        obj.save()

admin.site.register(Header, HeaderAdmin)