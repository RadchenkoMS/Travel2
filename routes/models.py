from django.core.exceptions import ValidationError
from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Маршрут')
    travel_time = models.SmallIntegerField(verbose_name='Час прибуття')
    from_town = models.ForeignKey(
        'cities.City',
        on_delete=models.CASCADE,
        related_name='routes_from_town_set',
        verbose_name='З міста')
    to_town = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='routes_to_town_set',
                                verbose_name='до міста')
    trains = models.ManyToManyField('trains.Train', verbose_name='Потяги')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'
        ordering = ['travel_time']

    def __str__(self):
        return f'Маршрут {self.name} з міста {self.from_town} до {self.to_town}'
