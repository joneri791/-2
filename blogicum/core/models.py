from django.db import models


class BaseModel(models.Model):
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')
    created_at = models.DateTimeField()

    class Meta():
        abstract = True