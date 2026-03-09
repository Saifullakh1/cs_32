from django.urls import path
from .views import UserRegisterAPIView, UserRetrieveAPIView


urlpatterns = [
    path('register', UserRegisterAPIView.as_view(), name='register'),
    path('user/<int:pk>', UserRetrieveAPIView.as_view(), name='update')
]