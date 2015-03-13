from django.shortcuts import render, get_object_or_404, get_list_or_404
from home.models import Theme
from article.models import Article


def index(request):
    current_header = get_object_or_404(Theme, current_theme=True)
    current_articles = get_list_or_404(Article.objects.order_by("-published_date"), published_status=True)[:3]
    context = {
        "theme": current_header,
        "current_articles": current_articles
    }
    return render(request, "home/index.html", context)