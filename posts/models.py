from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    photo_description = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_added = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title
