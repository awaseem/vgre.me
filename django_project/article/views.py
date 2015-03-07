from django.shortcuts import render, get_object_or_404, get_list_or_404 ,redirect
from article.models import Article
from home.models import Header
from watson import search as watsonSearch


def article(request, game_id):
    article_requested = get_object_or_404(Article, published_status=True, game_name=game_id)
    context = {
        "article": article_requested
    }
    return render(request, "article/article.html", context)


def search(request):
    if request.method == "POST":
        search_query = request.POST.get("search_query")
        if search_query:
            return redirect("results", search_query)
    return render(request, "article/reviews.html", getSearchContext())


def results(request, search_query):
    context = getSearchContext()
    search_results = watsonSearch(search_query)
    if search_results:
        context["results"] = search_results
    else:
        context["err_message"] = "Sorry! No Game Reviews Found :("
    return render(request, "article/reviews.html", context)


def getSearchContext():
    # Obtain search context for the search page, this logic is used twice. Hence its wrapped in a function
    current_header = get_object_or_404(Header, current_header=True)
    current_articles = get_list_or_404(Article.objects.order_by("-published_date"), published_status=True)[:9]
    context = {
        "current_header": current_header,
        "current_articles": current_articles,
    }
    return context