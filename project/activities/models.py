from django.db import models


class ActivityType(models.Model):
    """
    A type of activity that can be conducted by a participant.
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ParticipantRole(models.Model):
    """
    The role of a person who participates in an activity.
    """

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Activity(models.Model):
    """
    Represents an activity conducted by a person.
    """

    start = models.DateTimeField()
    end = models.DateTimeField()
    activity_type = models.ForeignKey(to=ActivityType, on_delete=models.PROTECT)
    participant_role = models.ForeignKey(to=ParticipantRole, on_delete=models.PROTECT)

    def __str__(self):
        return f"{ self.participant_role} - { self.activity_type }"

    class Meta:
        verbose_name_plural = "Activities"