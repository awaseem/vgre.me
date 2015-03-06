from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns("",

    url(r"^game/(?P<game_id>[\w ]+)/$", views.article, name="article"),
    url(r"^search/$", views.search, name="reviews"),
    url(r"^search/results/(?P<search_query>[\w ]+)/$", views.results, name="results"),

)