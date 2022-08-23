from django.core.exceptions import ValidationError
from django.db import models


class Train(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Потяг')
    travel_time = models.SmallIntegerField(verbose_name='Час прибуття')
    from_town = models.ForeignKey(
        'cities.City',
        on_delete=models.CASCADE,
        related_name='from_town_set',
        verbose_name='З міста')
    to_town = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='to_town_set',
                                verbose_name='до міста')

    class Meta:
        verbose_name = 'Потяг'
        verbose_name_plural = 'Потяги'
        ordering = ['travel_time']

    def __str__(self):
        return f'Потяг {self.name} з міста {self.from_town} до {self.to_town}'

    def clean(self):
        if self.from_town == self.to_town:
            raise ValidationError('Города не могут быть одинаковыми')
        qs = Train.objects.filter(
            from_town=self.from_town,
            to_town=self.to_town,
            travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Время пути не может быть одинаковым')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
