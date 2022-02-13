from django.db import models

# Create your models here.
class files(models.Model):
    fil = models.FileField(upload_to = 'home/files/')