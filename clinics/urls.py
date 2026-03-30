from django.urls import path
from .views import ClinicAPIView, ClinicRetrieveAPIView


urlpatterns = [
    path('', ClinicAPIView.as_view(), name='list'),
    path('<int:pk>', ClinicRetrieveAPIView.as_view(), name='retrieve')
]