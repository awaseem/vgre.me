from django.contrib import admin
from article.models import Article, Sections
from django.utils import timezone
# Register your models here.

COLOR_CODES = {
    "Blue": "#337ab7",
    "Green": "#5cb85c",
    "Yellow": "#f0ad4e",
    "Light Blue": "#5bc0de",
    "Red": "#d9534f"
}

class SectionsInLine(admin.StackedInline):
    model = Sections
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Game", {
            "fields": ["game_name", "game_review_description", "game_review_cover", "game_review_back_cover",
                       "game_theme"]
        }),
        ("Header", {
            "fields": ["article_heading", "article_sub_heading", "header_image"]
        }),
        ("Summary", {
            "fields": ["review_summary", "review_score", "footer_image"]
        })
    ]

    inlines = [SectionsInLine]

    list_display = ("create_date", "game_name", "review_status", "published_status", "published_date")

    list_filter = ("create_date", "game_name", "review_status", "published_status")

    actions = ["toggle_publish", "toggle_review"]

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
        for article in queryset:
            article.published_status = not article.published_status
            if article.published_status:
                article.published_date = timezone.now()
            else:
                article.published_date = None
            article.save()

    toggle_publish.short_description = "Publish/unpublish article"

    def toggle_review(self, request, queryset):
        for article in queryset:
            article.review_status = not article.review_status
            article.save()

    toggle_review.short_description = "Review/not review article"

    def save_model(self, request, obj, form, change):
        obj.game_menu_color = COLOR_CODES[obj.get_game_theme_display()]
        if not obj.created_user:
            obj.created_user = request.user.get_username()
            obj.created_name = request.user.get_full_name()
        else:
            obj.last_modified_user = request.user.get_username()
        obj.save()


admin.site.register(Article, ArticleAdmin)