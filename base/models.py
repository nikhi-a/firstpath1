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
    
class Company(models.Model):
        name = models.CharField(max_length=255)
        logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
        website = models.URLField(blank=True, null=True)
        description = models.TextField()
        location = models.CharField(max_length=255)
        created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Creator of the company page
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name