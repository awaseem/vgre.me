from django.conf.urls import patterns, url

from article import views

urlpatterns = patterns("",

    url(r"^(?P<game_id>[\w ]+)/$", views.article, name="article")

)