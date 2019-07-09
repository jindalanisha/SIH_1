from django.db import models


# Create your models here.
class OrganisationInfo(models.Model):
    orgnisation_name=models.CharField(max_length=30)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    email=models.EmailField()
    contact_no=models.DecimalField(max_digits=10,decimal_places=0)
    org_domain=models.CharField(max_length=150)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.orgnisation_name

class CapitalistInfo(models.Model):
    name=models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email=models.EmailField( max_length=254)
    contact_no = models.DecimalField(max_digits=10, decimal_places=0)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
