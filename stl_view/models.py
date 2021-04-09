from django.db import models

# Create your models here.
class Stl_view(models.Model):
  caseID = models.CharField(max_length=20)
  created_at = models.DateTimeField()