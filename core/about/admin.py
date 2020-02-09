from django.contrib import admin

from . import models


class EducationInline(admin.TabularInline):
    model = models.Education
    extra = 0


@admin.register(models.Profile)
class MeetingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
    )
    inlines = [EducationInline]
