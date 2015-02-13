from django.db import models
from django.utils.encoding import force_bytes
# Create your models here.


class Header(models.Model):
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    sub_heading = models.CharField(max_length=200)
    button_text = models.CharField(max_length=5, blank=False)
    title_text = models.CharField(max_length=200, blank=False)
    summary_text = models.CharField(max_length=400, blank=False)
    current_header = models.BooleanField(default=False)

    def __str__(self):
        return force_bytes("%s" % self.sub_heading)
