from django.db import models

# Create your models here.
class Artiste (models.Model):
    first_name = models.CharField (max_length=100)
    last_name = models.CharField (max_length=100) 
    age = models.DateField() 

    def __str__ (self):
        return self.first_name

class Song (models.Model):
    artiste = models.ForeignKey (Artiste, on_delete = models.CASCADE)
    title = models.CharField (max_length=100)
    date_released = models.IntegerField()
    likes = models.CharField (max_length=500)
    artiste_id = models.IntegerField()


    def __str__ (self):
        return self.title

class Lyric (models.Model):
    song = models.ForeignKey (Song, on_delete = models.CASCADE)
    content = models.CharField (max_length=500)
    song_id = models.IntergerField ()

    def __str__ (self):
        return self.song
