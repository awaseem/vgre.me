from django.conf.urls import patterns
from django.contrib import admin
from article.models import Article, Sections
from django.utils import timezone
from django.contrib.messages import constants as messages
from django.shortcuts import redirect
from article.views import article
# Register your models here.


class SectionsInLine(admin.StackedInline):
    model = Sections
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Game", {
            "fields": ["game_name", "game_review_description", "game_review_cover", "game_review_back_cover"]
        }),
        ("Header", {
            "fields": ["article_heading", "article_sub_heading", "header_image"]
        }),
        ("Summary", {
            "fields": ["review_summary", "review_score", "footer_image"]
        })
    ]

    inlines = [SectionsInLine]

    list_display = (
        "create_date", "game_name", "review_status", "published_status", "published_date", "last_modified_user")

    list_filter = ("create_date", "game_name", "review_status", "published_status")

    actions = ["toggle_publish", "toggle_review", "show_preview"]

    def get_urls(self):
        urls = super(ArticleAdmin, self).get_urls()
        preview_url = patterns("",
            (r"^preview/(?P<game>(.*))/$", self.admin_site.admin_view(self.preview_view))
        )
        return preview_url + urls

    def preview_view(self, request, game):
        return article(request, game, is_preview=True)

    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_user=request.user.get_username())

    def get_actions(self, request):
        actions = super(ArticleAdmin, self).get_actions(request)
        if request.user.is_superuser:
            return actions
        else:
            del actions["toggle_publish"]
        return actions

    def toggle_publish(self, request, queryset):
        for query in queryset:
            query.published_status = not query.published_status
            if query.published_status:
                query.published_date = timezone.now()
            else:
                query.published_date = None
            query.save()

    toggle_publish.short_description = "Publish/unpublish article"

    def toggle_review(self, request, queryset):
        for query in queryset:
            query.review_status = not query.review_status
            query.save()

    toggle_review.short_description = "Review/not review article"

    def show_preview(self, request, queryset):
        if len(queryset) == 1:
            for query in queryset:
                return redirect("preview/%s" % query.game_name)
        else:
            self.message_user(request, "ERROR: you can only show one page's preview", level=messages.ERROR)

    show_preview.short_description = "Article Preview"

    def save_model(self, request, obj, form, change):
        if not obj.created_user:
            obj.created_user = request.user.get_username()
        else:
            obj.last_modified_user = request.user.get_username()
        obj.save()

admin.site.register(Article, ArticleAdmin)