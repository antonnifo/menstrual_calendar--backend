from django.urls import path
from .views import UserSignupView, UserDetailView, UserEditView, UserDeleteView, UserLogoutView, CustomTokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login and get tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),  # Verify token validity
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'), 
    path('user/edit/<int:id>/', UserEditView.as_view(), name='user-edit'), 
    path('user/delete/<int:id>/', UserDeleteView.as_view(), name='user-delete'), 
]
