from django.db import models

# Create your models here.

class UserColumn(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(blank=False, null= False)
    Last_update_date = models.DateTimeField(auto_now=True)
    Last_update_by = models.IntegerField(blank=False, null= False)

    class Meta:
        abstract = True