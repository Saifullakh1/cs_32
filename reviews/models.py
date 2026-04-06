from django.db import models
from clinics.models import Clinic
from users.models import User


class Rating(models.Choices):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class Review(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="clinic_reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews")
    description = models.TextField()
    rating = models.IntegerField(default=0, choices=Rating.choices, verbose_name="Оценка")
    image = models.FileField(upload_to='reviews_images', blank=True, verbose_name="Картинка")

    def __str__(self):
        return self.description
