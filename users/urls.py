from django.urls import path
from .views import UserSignupView, UserLoginView, UserDetailView, UserEditView, UserDeleteView, UserLogoutView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'), 
    path('user/edit/', UserEditView.as_view(), name='user-edit'), 
    path('user/delete/', UserDeleteView.as_view(), name='user-delete'), 
]
