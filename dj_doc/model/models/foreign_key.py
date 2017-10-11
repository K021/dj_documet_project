from django.db import models


__all__ = (
    'Manufacturer',
    'Car',
    'User',
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} of {self.manufacturer.name}'


class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self == self.teacher:
            return
        # python3 에서는 그냥 super()로 가능하다.
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
