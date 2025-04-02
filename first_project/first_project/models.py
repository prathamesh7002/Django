from django.db import models

class user(models.Model):
    username=models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True) 
    password=models.CharField(max_length=100)
    language = models.CharField(max_length=50, null=True, blank=True, default='English')

    class Meta:
        db_table='user'

    def __str__(self):
        return self.username