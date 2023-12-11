from django.db import models

# Create your models here.
class Visitor(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.first_name
    