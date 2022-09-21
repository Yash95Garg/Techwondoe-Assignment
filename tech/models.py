import uuid
from django.db import models
from datetime import date, datetime

# Create your models here.
from django.contrib.auth.models import User


class Company(models.Model):
    CompanyID = models.UUIDField(primary_key=True,default=uuid.uuid4)
    CompanyName = models.CharField(max_length=100)
    CompanyCEO = models.CharField(max_length=55)
    CompanyAddress = models.CharField(max_length=250)
    InceptionDate = models.DateTimeField(default=datetime.now())
    class Meta:
        ordering = ['-InceptionDate']

    def __str__(self):
        return self.CompanyName

class Team(models.Model):
    TeamID = models.UUIDField(primary_key=True,default=uuid.uuid4)
    CompanyID = models.ForeignKey(Company, on_delete= models.CASCADE,related_name='team_details')
    TeamLead = models.CharField(max_length=55)
    def __str__(self):
        return self.TeamLead
