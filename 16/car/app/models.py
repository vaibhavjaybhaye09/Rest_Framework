from django.db import models

# Create your models here.
class Car(models.Model):
    Model = models.CharField(max_length=100)
    No  = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    crearted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
       ordering = ['-created_at']

    def __str__(self):
        return self.Model
   