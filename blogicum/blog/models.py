from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(BaseModel): # Тематическая категория
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)

class Location(BaseModel):
    name = models.CharField(max_length=256)

class Post(BaseModel): # Публикация
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.SET_NULL,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
    )

