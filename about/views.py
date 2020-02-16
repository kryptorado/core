import logging

from rest_framework import mixins, permissions, response, status, viewsets

from . import serializers
from .models import Profile


logger = logging.getLogger(__name__)


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ProfileSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Profile.objects.all()
