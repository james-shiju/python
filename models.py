from django.db import models


class Contact(models.Model):
    """data for storage"""
    # id = models.AutoField()
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    objects = models.Manager()

    # class Meta:
    #     verbose_name = "Data"
    #     verbose_name_plural = "Datas"
    
    # def __str__(self):
    #     return self.name

class IContact(models.Model):
    """A model of a IContact"""

    name = models.ForeignKey(Contact, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, default=1)

    # def __str__(self):
    #     return self.name.name
