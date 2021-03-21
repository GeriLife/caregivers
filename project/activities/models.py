from django.db import models


class ActivityType(models.Model):
    """
    A type of activity that can be conducted by a participant.
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
