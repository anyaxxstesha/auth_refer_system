from django.urls import path

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('auth/get_code/', views.UserGetCodeAPIView.as_view(), name='get_code'),

    path('auth/send_code/', TokenObtainPairView.as_view(), name='send_code'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
