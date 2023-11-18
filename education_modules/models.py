from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class EducationalModule(models.Model):
    """
        Модель для представления образовательных модулей.
    """
    order_number = models.PositiveIntegerField(
        unique=True, verbose_name='Порядковый номер')
    title = models.CharField(
        max_length=255, verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный курс')
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, blank=True,
        verbose_name='Аватар')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return self.title


class Review(models.Model):
    """
        Модель для представления отзывов к образовательным модулям.
    """
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='Автор отзыва')
    educational_module = models.ForeignKey(EducationalModule,
                                           on_delete=models.CASCADE,
                                           related_name='reviews',
                                           verbose_name='Образовательный '
                                                        'модуль')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата и время создания')

    def __str__(self):
        return f"Отзыв от {self.author} на модуль " \
               f"{self.educational_module.title}"
