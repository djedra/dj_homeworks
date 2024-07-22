# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


    def post(self, request):
        name = request.GET['name']
        description = request.GET['description']
        Sensor.objects.create(name=name, description=description)
        return Response({'status': 'OK'})

    def patch(self, request):
        id = request.GET['id']
        name = request.GET['name']
        description = request.GET['description']
        Sensor.objects.filter(id=id).update(name=name, description=description)
        return Response({'status': 'OK'})


class SensorIdView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        id = request.GET['id']
        temperature = request.GET['temperature']
        sensor = Sensor.objects.get(id=id)
        sensor.measurements.create(temperature=temperature)
        return Response({'status': 'OK'})

class MeasurementIdView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer