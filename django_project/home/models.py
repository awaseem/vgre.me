from django.db import models
from django.utils.encoding import force_bytes
from tinymce.models import HTMLField
# Create your models here.


class Theme(models.Model):
    THEME_COLOR = (
        ("btn-primary", "Blue"),
        ("btn-success", "Green"),
        ("btn-info", "Light Blue"),
        ("btn-warning", "Yellow"),
        ("btn-danger", "Red")
    )

    pub_date = models.DateTimeField("date published", auto_now_add=True)
    theme_name = models.CharField(max_length=50, blank=False, help_text="Give this theme a name")
    theme_choice = models.CharField(max_length=20, choices=THEME_COLOR, default="btn-primary", blank=False,
                                    verbose_name="Theme", help_text="Color theme for the featured game")
    menu_background = models.CharField(max_length=10, default="#337ab7")
    home_header_cover = models.URLField(blank=False,
                                        help_text="Please enter A URL of a picture you'd like for the home page header")
    home_footer_cover = models.URLField(blank=False,
                                        help_text="Please enter a URL of a picture you'd like for the home page footer")
    search_header_cover = models.URLField(blank=False,
                                          help_text="Please enter a URL of a picture you'd like for the search page header")
    search_footer_cover = models.URLField(blank=False,
                                          help_text="Please enter a URL of a picture you'd like for the search page footer")
    current_theme = models.BooleanField(default=False)

    def __str__(self):
        return force_bytes("%s" % self.theme_name)
