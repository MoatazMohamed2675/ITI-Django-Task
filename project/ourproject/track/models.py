from django.db import models

# Create your models here.

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    status=models.BooleanField(default=True)
    @classmethod
    def getalltracks(cls):
        return cls.objects.all()

    @classmethod
    def gettrackbyid(cls,id):
        return cls.objects.get(id=id)