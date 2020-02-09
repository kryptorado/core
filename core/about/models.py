from django.db import models


class Profile(models.Model):
    '''
    A model to contain information about myself.
    '''
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    school_name = models.CharField(max_length=256, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    major = models.CharField(max_length=256, blank=True)
    degree_type = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f'Profile: {self.profile}'

