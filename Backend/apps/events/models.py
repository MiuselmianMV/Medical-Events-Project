from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify


class Specialty(models.Model):
    """Модель медицинской специальности."""
    class Meta:
        db_table = "specialties"
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

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
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['scheduled_date', 'scheduled_time']

    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()
    location = models.CharField(max_length=200)
    duration = models.DurationField()
    specialties = models.ManyToManyField(Specialty, related_name='events')
    card_id = models.ForeignKey('Card', on_delete=models.SET_NULL, null=True, blank=True, related_name='events')

    class EventType(models.TextChoices):
        ONLINE = 'online', 'Онлайн'
        OFFLINE = 'offline', 'Офлайн'
        MIXED = 'mixed', 'Змішаний'

    event_type = models.CharField(max_length=10, choices=EventType.choices, default=EventType.OFFLINE)

    class Status(models.TextChoices):
        PLANNED = "planned", "Planned"
        DONE = "done", "Done"
        CANCELED = "canceled", "Canceled"
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PLANNED)

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
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    title = models.CharField(max_length=200)
    photo_url = models.URLField()
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


