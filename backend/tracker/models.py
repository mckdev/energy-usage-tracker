from django.db import models
from django.utils import timezone


class Reading(models.Model):
    user = models.ForeignKey(
        'auth.User', related_name='readings', on_delete=models.CASCADE)
    date = models.DateTimeField('reading date', blank=True)
    value = models.FloatField()

    class Meta:
        ordering = ('date',)

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()
        super().save(*args, **kwargs)
