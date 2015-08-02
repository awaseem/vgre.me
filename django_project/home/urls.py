from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',

    # Url routing for the home page
    url(r'^$', views.index, name="index")

)