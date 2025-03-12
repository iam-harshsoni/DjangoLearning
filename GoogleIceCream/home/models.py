from django.db import models
from django.contrib.auth.models import User


"""
makemigrations = create changes and store them in a file
migrations = apply the pending changes created by makemigrations
""" 

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.email}"
        