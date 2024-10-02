from django.db import models
import uuid

# Create your models here.
class Artist(models.Model):
    picture = models.FileField()
    artist_name = models.CharField(null=False, max_length=20, blank = False)
    biography= models.CharField(max_length=500, null=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable= False)
    
    
    def __str__(self):
        return self.artist_name

class Songs(models.Model):
    artists = models.ManyToManyField(Artist)  
    title = models.CharField(blank=True, max_length=20)
    youtube_link = models.URLField(blank=True)
    spotify_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title