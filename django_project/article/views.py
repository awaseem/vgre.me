from django.shortcuts import render, get_object_or_404
from home.models import Header
from article.models import Article


def article(request, game_id):
    article_requested = get_object_or_404(Article, published_status=True, game_name=game_id)
    context = {
        "article": article_requested
    }
    return render(request, "article/article.html", context)
