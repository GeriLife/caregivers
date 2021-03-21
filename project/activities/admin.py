from django.contrib import admin

from .models import (
    Activity,
    ActivityType,
    ParticipantRole,
)


@admin.register(Activity)
class ActivityModelAdmin(admin.ModelAdmin):
    fields = ("participant_role", "activity_type", "start", "end")
    list_display = ("participant_role", "activity_type", "start", "end")
    date_hierarchy = 'start'


@admin.register(ActivityType)
class ActivityTypeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(ParticipantRole)
class ParticipantRoleModelAdmin(admin.ModelAdmin):
    pass
