from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Feature(models.Model):
    title = CharField(max_length=100)
    description = CharField
