from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')

    class Meta:
        verbose_name = 'датчик'
        verbose_name_plural = 'датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'измерение'
        verbose_name_plural = 'измерения'

    def __str__(self):
        return self.temperature
