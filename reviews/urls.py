from django.urls import path
from .views import ReviewAPIView, ReviewRetrieveAPIView


urlpatterns = [
    path('', ReviewAPIView.as_view(), name='create'),
    path('<int:pk>/', ReviewRetrieveAPIView.as_view(), name='retrieve')
]