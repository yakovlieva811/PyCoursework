from django.db import models

# Create your models here.
from django.db import models


class School(models.Model):
    SchoolId = models.CharField(max_length=4)
    SchoolName = models.CharField(max_length=300)
    SchoolAddress = models.CharField(max_length=300)

    class Meta:
        db_table = "PySchools"
