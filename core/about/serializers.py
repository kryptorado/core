from rest_framework import serializers
from . import models



class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = (
            'name',
            'start_date',
            'end_date',
        )
        read_only_fields = fields

    def validate(self, data):
        return data


class ProfileSerializer(serializers.ModelSerializer):
    education = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = (
            'id',
            'first_name',
            'last_name',
            'education',
        )
        read_only_fields = fields

    def get_education(self, obj):
        if obj.education_set.exists():
            return EducationSerializer(
                obj.education_set.first()
            ).data
        return None
