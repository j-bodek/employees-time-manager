from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=200, blank=True, null=True)
    table_row = models.IntegerField()
    presence = models.IntegerField()
    E01 = models.IntegerField()
    E02 = models.IntegerField()
    E03 = models.IntegerField()
    E04 = models.IntegerField()
    E05 = models.IntegerField()
    E06 = models.IntegerField()
    E07 = models.IntegerField()
    E08 = models.IntegerField()
    E09 = models.IntegerField()
    E10 = models.IntegerField()