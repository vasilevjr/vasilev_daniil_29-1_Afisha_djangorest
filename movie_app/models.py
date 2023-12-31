from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text =models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1,6)])

    def __str__(self):
        return self.text


