from django.shortcuts import render, get_object_or_404, get_list_or_404
from home.models import Theme
from article.models import Article


def index(request):
    """
    View to call when a user hits the home url.
    :param request: a request object from a url route a visitor is hit
    :return: web page with all information regarding the home page
    """
    # Get the current theme object, if no object is found throw a 404
    current_header = get_object_or_404(Theme, current_theme=True)
    # Get three of the latest articles ordered by publish date and display them as recent reviews
    current_articles = get_list_or_404(Article.objects.order_by("-published_date"), published_status=True)[:3]
    # Create context with the current_header and current_articles for django template tags to process
    context = {
        "theme": current_header,
        "current_articles": current_articles
    }
    return render(request, "home/index.html", context)