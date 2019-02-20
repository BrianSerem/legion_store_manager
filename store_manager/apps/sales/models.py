from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class TimeStamped(models.Model):
    """
    Creation time and update timestamps
    """
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Sale(TimeStamped):
	"""This class defines a sale instance"""
    attendant = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)
