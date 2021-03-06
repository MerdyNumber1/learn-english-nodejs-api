from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import SimpleRouter

from .views import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet, basename='profile')

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='profile-get-token'),
    path(
        'token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='profile-token-refresh',
    ),
    *router.urls,
]
