from django.shortcuts import render, get_object_or_404, get_list_or_404
from home.models import Header
from article.models import Article


def index(request):
    current_header = get_object_or_404(Header, current_header=True)
    current_articles = get_list_or_404(Article.objects.order_by("-published_date"), published_status=True)[:3]
    context = {"current_header": current_header, "current_articles": current_articles}
    return render(request, "home/index.html", context)