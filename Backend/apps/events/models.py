from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify


class Specialty(models.Model):
    """Модель медицинской специальности."""
    class Meta:
        db_table = "specialties"
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    name = models.CharField(max_length=100, unique=True, verbose_name="Назва")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Event(models.Model):
    """Модель медицинского события."""
    class Meta:
        db_table = "events"
        verbose_name = "Подія"
        verbose_name_plural = "Події"
        ordering = ['scheduled_date', 'scheduled_time']

    title = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    slug = models.SlugField(max_length=100, unique=True)

    scheduled_date = models.DateField(verbose_name="Дата проведення")
    scheduled_time = models.TimeField(verbose_name="Час проведення")
    location = models.CharField(max_length=200, verbose_name="Місце проведення")
    duration = models.DurationField(verbose_name="Тривалість")
    specialties = models.ManyToManyField(Specialty, related_name='events', verbose_name="Спеціальності")
    card = models.ForeignKey('Card', on_delete=models.SET_NULL, null=True, blank=True, related_name='events', verbose_name="Карточка")
    form_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Посилання на гугл-форму")

    class EventType(models.TextChoices):
        ONLINE = 'online', 'Онлайн'
        OFFLINE = 'offline', 'Офлайн'
        MIXED = 'mixed', 'Змішаний'

    event_type = models.CharField(max_length=10, choices=EventType.choices, default=EventType.OFFLINE, verbose_name="Тип події")

    class Status(models.TextChoices):
        PLANNED = "запланований", "Запланований"
        DONE = "завершений", "Завершений"
        CANCELED = "відмінений", "Відмінений"

    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PLANNED, verbose_name="Статус")

    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Card(models.Model):
    """Модель карточки, связанной с медицинским событием."""
    class Meta:
        db_table = "cards"
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

    title = models.CharField(max_length=200, verbose_name="Назва")
    photo_url = models.URLField(verbose_name="Посилання на зображення")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


