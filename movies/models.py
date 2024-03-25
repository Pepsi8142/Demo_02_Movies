from django.db import models

# Create your models here.


class MovieData(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(blank=True)
    genre = models.CharField(max_length=20, blank=True)
    director = models.CharField(max_length=50, blank=True)
    duration = models.FloatField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='Images/', default="Images/default.jpg")

    def __str__(self):
        return self.title

