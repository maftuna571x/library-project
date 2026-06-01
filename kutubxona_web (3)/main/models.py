"""
Kutubxona modellari — Templates va render() darsi uchun.
"""

from django.db import models


class Muallif(models.Model):
    """Kitob muallifi."""
    ism_familiya = models.CharField(max_length=100)
    tugilgan_yili = models.IntegerField()
    shahar = models.CharField(max_length=50)
    bio = models.TextField(blank=True, default='')

    def __str__(self):
        return self.ism_familiya
 

class Kitob(models.Model):
    """Kutubxonadagi kitob."""
    nom = models.CharField(max_length=200)
    muallif = models.ForeignKey(
        Muallif,
        on_delete=models.CASCADE,
        related_name='kitoblari'
    )
    yil = models.IntegerField()
    narx = models.IntegerField()
    mavjud = models.BooleanField(default=True)
    qoshilgan = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom
