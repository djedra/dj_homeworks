from django.urls import path
from measurement.views import SensorView, SensorIdView, MeasurementView, MeasurementIdView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view()),
    path('sensor/<pk>', SensorIdView.as_view()),
    path('measurement/', MeasurementView.as_view()),
    path('measurement/<pk>', MeasurementIdView.as_view()),

]