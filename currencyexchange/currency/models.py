from django.db import models

# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    def __repr__(self):
        return f'{self.name} ({self.code})'
    def __str__(self):
        return self.code


class Rate(models.Model):
    currency_from = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='+')
    currency_to = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='+')
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4)

    def __str__(self):
        return f'{self.currency_from.code} -> {self.currency_to.code}: {self.rate}'

