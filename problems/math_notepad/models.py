from django.db import models

class Note(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField("Tag")
    creation_date = models.DateTimeField()
    deleted = models.BooleanField()
    def __unicode__(self):
        return self.text
 
class Tag(models.Model):
    name = models.CharField(max_length=256)
    def __unicode__(self):
        return self.name
