from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article
from watson import search as watsonSearch


def article(request, game_id):
    article_requested = get_object_or_404(Article, published_status=True, game_name=game_id)
    context = {
        "article": article_requested
    }
    return render(request, "article/article.html", context)


def search(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query", None)
        return redirect("results", search_query)
    else:
        return render(request, "article/reviews.html")


def results(request, search_query):
    print search_query
    search_results = watsonSearch(search_query)
    context = {
        "results": search_results
    }
    return render(request, "article/reviews.html", context)