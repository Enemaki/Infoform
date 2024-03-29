from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    job = models.TextField()
    
    def __str__(self):
        return self.name

    