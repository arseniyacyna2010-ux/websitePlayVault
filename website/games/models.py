from django.db import models

class Game(models.Model):
    name2 = models.CharField(max_length=200)
    description = models.TextField()
    image2 = models.ImageField(upload_to='game_images/', blank=True, null=True)
    download_link = models.FileField(upload_to='game_downloads/', blank=True, null=True)

    def __str__(self):
        return  self.name2
