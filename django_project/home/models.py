from django.db import models
from django.utils.encoding import force_bytes
from tinymce.models import HTMLField
# Create your models here.


class Header(models.Model):

    THEME_COLOR = (
        ("btn-primary", "Blue"),
        ("btn-success", "Green"),
        ("btn-info", "Light Blue"),
        ("btn-warning", "Yellow"),
        ("btn-danger", "Red")
    )

    pub_date = models.DateTimeField("date published", auto_now_add=True)
    theme_name = models.CharField(max_length=50, blank=False, help_text="Give this theme a name")
    main_heading = models.CharField(max_length=10, blank=False, help_text="Please enter a main header")
    sub_heading = models.CharField(max_length=200, blank=False, help_text="Please enter a sub heading")
    title_text = models.CharField(max_length=200, blank=False,
                                  help_text="Please enter a heading for the reviews section")
    summary_text = HTMLField(blank=False, help_text="Please enter a summary for the reviews section")
    theme_choice = models.CharField(max_length=20, choices=THEME_COLOR, default="btn-primary", blank=False,
                                    verbose_name="Theme", help_text="Color theme for the featured game")
    menu_background = models.CharField(max_length=10, default="#337ab7")
    header_cover = models.URLField(blank=False, help_text="Please enter A URL of a picture you'd like for the header")
    footer_cover = models.URLField(blank=False, help_text="Please enter a URL of a picture you'd like for the footer")
    current_header = models.BooleanField(default=False)

    def __str__(self):
        return force_bytes("%s" % self.sub_heading)
