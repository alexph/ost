from django.db import models


class Episode(models.Model):
    title = models.TextField()
    episode_number = models.IntegerField()
    created_at = models.DateTimeField()
    hero_image = models.ImageField()

    class Meta:
        ordering = ['episode_number']

    def __str__(self):
        return '{} - #{}'.format(self.title, self.episode_number)
