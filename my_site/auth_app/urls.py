from .views import RegisterView, LoginView, LogoutView, UserProfileMeViewSet
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', UserProfileMeViewSet.as_view(), name='profile')
]