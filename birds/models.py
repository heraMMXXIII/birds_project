from django.db import models

class Bird(models.Model):
    name = models.CharField(max_length=100)  # Имя птицы
    image = models.ImageField(upload_to='birds_images/')  # Фото птицы
    sound = models.FileField(upload_to='bird_sounds/', null=True, blank=True)  # Звук
    wiki_link = models.URLField()  # Ссылка на Википедию

    def __str__(self):
        return self.name

# Create your models here.
