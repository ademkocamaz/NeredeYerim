from django.db import models


# Create your models here.
class City(models.Model):
    
    name = models.CharField(
        verbose_name="Şehir",
        max_length=500,
    )

    class Meta:
        verbose_name="Şehir"
        verbose_name_plural="Şehirler"


class Restaurant(models.Model):
    name = models.CharField(
        verbose_name="Lokanta/Restoran",
        max_length=500,
    )

    class Meta:
        verbose_name="Lokanta/Restoran"
        verbose_name_plural="Lokantalar/Restoranlar"


class Food(models.Model):
    name = models.CharField(
        verbose_name="Yemek",
        max_length=500,
    )

    city = models.ForeignKey(
        verbose_name="Şehir",
        to=City,
        on_delete=models.DO_NOTHING,
        related_name="food_city",
    )

    restaurant = models.ForeignKey(
        verbose_name="Lokanta/Restoran",
        to=Restaurant,
        on_delete=models.DO_NOTHING,
        related_name="food_restaurant",
    )

    def __str__(self):
        return (
            "Yemek: "
            + self.name
            + " Şehir: "
            + self.city
            + " Lokanta/Restorant: "
            + self.restaurant
        )
    
    class Meta:
        verbose_name="Yemek"
        verbose_name_plural="Yemekler"
