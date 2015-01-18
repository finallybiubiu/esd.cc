from django.db import models

class Segmentfault(models.Model):
    qid = models.BigIntegerField(max_length=16)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=300)
    mark = models.IntegerField(max_length=10)
    view = models.IntegerField(max_length=10)
    follow = models.IntegerField(max_length=10)
    date = models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title
