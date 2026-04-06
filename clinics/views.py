from rest_framework import generics
from .models import Clinic
from .serializers import ClinicSerializer, ClinicRetrieveSerializer


class ClinicAPIView(generics.ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ClinicRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClinicRetrieveSerializer
        else:
            return self.serializer_class

