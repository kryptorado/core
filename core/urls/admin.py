from django.contrib import admin
from django.urls import include, path


admin_urlpatterns = [
    path('', admin.site.urls),
]

urlpatterns = [path('admin/', include(admin_urlpatterns))]
