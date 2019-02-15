from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=50)
    msg = models.CharField(max_length=200)
    image = models.ImageField('uploaded image' ,null=True)

    def __str__(self):
        return self.msg
