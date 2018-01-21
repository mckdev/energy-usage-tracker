from django.db import models


class Reading(models.Model):
    date = models.DateTimeField('reading date', auto_now_add=True)
    value = models.FloatField()

    class Meta:
        ordering = ('date',)
