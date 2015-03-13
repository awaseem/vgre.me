from django.db import models
from tinymce.models import HTMLField
from django.utils.encoding import force_bytes
# Create your models here.


class Article(models.Model):

    SCORE_CHOICES = zip(range(0, 11), range(0, 11))

    created_user = models.CharField(max_length=200, blank=True)
    last_modified_user = models.CharField(max_length=200, blank=True)
    created_name = models.CharField(max_length=200, blank=True)
    created_image = models.URLField(blank=True)
    created_occupation = models.CharField(max_length=100, blank=True)

    create_date = models.DateTimeField("Date created", auto_now_add=True)
    published_date = models.DateTimeField("Date published", null=True)

    review_status = models.BooleanField(default=False)
    published_status = models.BooleanField(default=False)

    game_name = models.CharField(max_length=100, blank=False, help_text="Name of the game you are reviewing")
    game_review_description = models.CharField(max_length=100, blank=False,
                                               help_text="Enter a short description about the game review (homepage)")
    game_review_cover = models.URLField(blank=False, help_text="Enter an image for the game cover (homepage)")
    game_review_back_cover = models.URLField(blank=False, help_text="Enter an image for the back game cover (homepage)")

    header_image = models.URLField(blank=False, help_text="Enter the URL for a header image")
    article_heading = models.CharField(max_length=50, blank=False, help_text="Article heading")
    article_sub_heading = models.CharField(max_length=50, blank=False, help_text="Article sub heading")

    footer_image = models.URLField(blank=False, help_text="Enter the URL for a footer image")
    review_summary = models.TextField(blank=False, help_text="Enter a summary for this game review")
    review_score = models.IntegerField(blank=False, help_text="Enter a review score for this game",
                                       choices=SCORE_CHOICES)

    def __str__(self):
        return force_bytes("%s" % self.game_name)


class Sections(models.Model):
    article = models.ForeignKey(Article)
    section_heading = models.CharField(max_length=50, blank=True, help_text="This sections heading")
    section_body = HTMLField(blank=True, help_text="Enter a paragraph for this section")
    image_url = models.URLField(blank=True, help_text="Enter the URL for this sections image ")
    image_subheading = models.CharField(blank=True, max_length=100,
                                        help_text="Enter the sub-heading for this sections image")
    gif_url = models.URLField(blank=True, help_text="Enter the URL for this sections gif (html video only)")
    gif_subheading = models.CharField(blank=True, max_length=100,
                                      help_text="Enter the sub-heading for this sections gif")