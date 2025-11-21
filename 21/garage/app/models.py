from django.db import models

# Create your models here.
class Garage(models.Model):
    SERVICES_CHOICE = (
        ('oil','OIL'),
        ('breake' , 'BREAKE'),
        ('light'  ,'LIGHT')       
    )
    name = models.CharField(max_length=100)
    loction = models.TextField()
    services = models.CharField(max_length=10, choices=SERVICES_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name