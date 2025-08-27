from django.db import models

from track.models import Track

# Create your models here.

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='trainee/images/')
    status=models.BooleanField(default=True)
    trackid=models.ForeignKey(Track, on_delete=models.CASCADE)

    @classmethod
    def getalltrainees(cls):
        return cls.objects.all()

    @classmethod
    def gettraineebyid(cls,id):
        return cls.objects.get(id=id)