from django.db import models
from core.models import BaseModel


class ShortenedURL(BaseModel):
    """
    Model representing a shortened URL.
    """
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)
