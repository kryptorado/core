from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()

router.register('', views.ProfileViewSet, base_name='profile')

urlpatterns = [path('profile/', include(router.urls))]
