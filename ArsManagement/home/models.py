from django.db import models

class Slider(models.Model):
    sname = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='sliders', default='fallback.png', blank=True)

    def __str__(self):
        return self.sname
class Categoryicons(models.Model):
    iname = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='icons', default='fallback.png', blank=True)