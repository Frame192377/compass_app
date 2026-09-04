from django.urls import path, include

urlpatterns = [
    path('openid/', include('oidc_provider.urls', namespace='openid')),
]