from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ReactionEntry(models.Model):
    """
    Reaction entry in a Timeline
    """
    episode = models.ForeignKey('episodes.Episode', related_name='reactions')

    user = models.ForeignKey(User)
    created_at = models.DateTimeField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('content_type', 'object_id')
        ordering = ['-created_at']


class AbstractReaction(models.Model):
    # user = models.ForeignKey(User)
    # created_at = models.DateTimeField()

    # Sorry, I've changed all the things.

    class Meta:
        abstract = True

    @property
    def entry(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        try:
            return ReactionEntry.objects.get(content_type=content_type, object_id=self.pk)
        except ReactionEntry.DoesNotExist:
            return None

    @property
    def deleted(self):
        if self.entry:
            return self.entry.deleted

    def delete(self, using=None):
        if self.entry:
            self.entry.delete()
        return super().delete(using)


class ImageReaction(AbstractReaction):
    image = models.ImageField()

    def __str__(self):
        return self.image.url


class TweetReaction(AbstractReaction):
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.text
