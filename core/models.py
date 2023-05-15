from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    Abstract base model for other models.
    """
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
