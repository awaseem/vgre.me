from django.db import models
from django.utils.encoding import force_bytes


class Theme(models.Model):
    """
    This model stores data about the websites overall theme.
    Writers can create any theme they would like as long as all
    fields are completed
    """

    # Colors for the main theme, changes menu background as well as highlight and button colors
    THEME_COLOR = (
        ("btn-primary", "Blue"),
        ("btn-success", "Green"),
        ("btn-info", "Light Blue"),
        ("btn-warning", "Yellow"),
        ("btn-danger", "Red")
    )

    # General name for the theme
    theme_name = models.CharField(max_length=50, blank=False, help_text="Give this theme a name")

    # Date the theme was published by a writer
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    # Information about the current theme color, menu background get populated when the user picks a theme
    theme_choice = models.CharField(max_length=20, choices=THEME_COLOR, default="btn-primary", blank=False,
                                    verbose_name="Theme", help_text="Color theme for the featured game")
    menu_background = models.CharField(max_length=10, default="#337ab7")

    # Images for the home header and footer
    home_header_cover = models.URLField(blank=False,
                                        help_text="Please enter A URL of a picture you'd like for the home page header")
    home_footer_cover = models.URLField(blank=False,
                                        help_text="Please enter a URL of a picture you'd like for the home page footer")

    # Images for the search header anf footer
    search_header_cover = models.URLField(blank=False,
                                          help_text="Please enter a URL of a picture you'd like for the search page header")
    search_footer_cover = models.URLField(blank=False,
                                          help_text="Please enter a URL of a picture you'd like for the search page footer")

    # Boolean that indicates if this is the current field
    current_theme = models.BooleanField(default=False)

    def __str__(self):
        return force_bytes("%s" % self.theme_name)
