from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='имя')
    description = models.CharField(max_length=100, default='без описания', verbose_name='описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', max_length=10, verbose_name='сенсор')
    temperature = models.DecimalField(decimal_places=2, max_digits=5, verbose_name='температура', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата\время измерения')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return self.sensor.name