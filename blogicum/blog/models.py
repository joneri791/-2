from django.contrib.auth import get_user_model
from django.db import models


MAX_NAME_LENGTH = 25
User = get_user_model()


class CommonFieldsModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True)

    class Meta():
        abstract = True

    def __str__(self):
        return (f'Статус публикации: {self.is_published}, '
                f'Дата создания: {self.created_at}')


class Category(CommonFieldsModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, '
                   'цифры, дефис и подчёркивание.'),
        max_length=128)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return (f'Заголовок: {self.title[:MAX_NAME_LENGTH]}, '
                f'Описание: {self.description}, '
                f'Слаг: {self.slug}')


class Location(CommonFieldsModel):
    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return (f'Имя: {self.name[:MAX_NAME_LENGTH]}')


class Post(CommonFieldsModel):  # Публикация
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='author_posts')
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name='Местоположение',
        related_name='post_location'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='post_in_category'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return (f'Заголовок: {self.title[:MAX_NAME_LENGTH]}, '
                f'Текст: {self.text}, '
                f'Дата публикации: {self.pub_date}, '
                f'Автор: {self.author}, '
                f'Место публикации: {self.location}, '
                f'Категория публикации: {self.category}')
