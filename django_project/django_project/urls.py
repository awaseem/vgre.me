from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Main home page url route
    url(r"^", include("home.urls")),
    # Url route for the about section
    url(r"^about/", include("about.urls")),
    # Url route for all articles and also the search page
    url(r"^reviews/", include("article.urls")),
    # Url route for the admin page
    url(r'^admin/', include(admin.site.urls)),

    # Module
    (r'^tinymce/', include('tinymce.urls')),
)
