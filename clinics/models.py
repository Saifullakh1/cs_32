from django.db import models


class Clinic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="О клинике")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=50, verbose_name="Номер телефона")
    image = models.FileField(upload_to="clinic_image", blank=True, verbose_name="Картинка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Клиника"
        verbose_name_plural = "Клиники"