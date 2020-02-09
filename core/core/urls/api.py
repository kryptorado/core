from django.urls import include, path

API_APP_NAME = 'api'

api_patterns = [
    path('', include('about.urls')),
]

urlpatterns = [path('api/v1/', include((api_patterns, API_APP_NAME), namespace='v1'))]
