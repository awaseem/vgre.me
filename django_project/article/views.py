from django.shortcuts import render, get_object_or_404
from home.models import Header
from article.models import Article


def article(request):
    article_requested = get_object_or_404(Article)
    current_header_requested = get_object_or_404(Header, current_header=True)
    context = {
        "article": article_requested,
        "current_header": current_header_requested,
    }

    return render(request, "article/article.html", context)
