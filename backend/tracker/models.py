from django.db import models


class Reading(models.Model):
    user = models.ForeignKey(
        'auth.User', related_name='readings', on_delete=models.CASCADE)
    date = models.DateTimeField('reading date', auto_now_add=True)
    value = models.FloatField()

    class Meta:
        ordering = ('date',)
