from django.db import models

class File(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name