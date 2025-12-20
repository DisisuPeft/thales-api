from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    ProfileView
)

urlpatterns = [
    path("auth/sign/", CustomTokenObtainPairView.as_view()),
    path("auth/refresh/", CustomTokenRefreshView.as_view()),
    path("auth/verify/", CustomTokenVerifyView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('user/me/', ProfileView.as_view()),
]
