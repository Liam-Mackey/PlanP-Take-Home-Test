import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import status
from urllib.request import Request, urlopen
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from .models import Appointment

class GetDeleteUpdateAppointments(RetrieveUpdateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self, pk):
        queryset = self.queryset
        return queryset

    def get(self, request, pk):
        try:
            data = Appointment.objects.filter(id=pk).first()
        except Appointment.DoesNotExist:
            raise NotFound('This appointment does not exist.')
        data = model_to_dict(data)
        return Response(json.dumps(data, cls=DjangoJSONEncoder), status=status.HTTP_200_OK)

    def post(self, request, pk):
        pass

    def delete(self, request, pk):
        try:
            data = Appointment.objects.filter(id=pk).first()
        except Appointment.DoesNotExist:
            raise NotFound('This appointment does not exist.')
        self.serializer_class.destroy(self, data)
        return Response("Deleted", status=status.HTTP_200_OK)

class GetPostAppointments(ListCreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def get(self, request):
        data_arr = list()
        for app in Appointment.objects.all():
            data_app = model_to_dict(app)
            data_arr.append(data_app)


        return Response(json.dumps(data_arr, cls=DjangoJSONEncoder), status=status.HTTP_200_OK)

    def post(self, request):
        serializer_context = {'request': request}

        print(request.data)
        serializer_data = request.data

        serializer = self.serializer_class.create(self, serializer_data)
        return Response(json.dumps(serializer), status=status.HTTP_200_OK)


    