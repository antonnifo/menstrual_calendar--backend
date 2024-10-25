from django.urls import path
from .views import CustomTokenObtainPairView, UserSignupView, UserDetailView, UserEditView, UserDeleteView, UserLogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login and get tokens
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login and get tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify token validity
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'), 
    path('user/edit/', UserEditView.as_view(), name='user-edit'), 
    path('user/delete/', UserDeleteView.as_view(), name='user-delete'), 
]
