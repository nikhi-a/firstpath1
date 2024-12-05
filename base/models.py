from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    jobtitle = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    location = models.TextField(null = True, blank = True)
    compname = models.TextField(null = True, blank = True)
    compdesc = models.TextField(null = True, blank = True)
    complocation = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.jobtitle