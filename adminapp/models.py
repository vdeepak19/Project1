from django.db import models

# Create your models here.
class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    comments = models.TextField(max_length=255)
    class Meta:
        db_table="contactus"