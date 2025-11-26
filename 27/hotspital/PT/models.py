from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    name = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(120)
        ]
    )

    admitted_on = models.DateField(auto_now_add=True)
    discharged_on = models.DateField(null=True, blank=True)
    is_discharged = models.BooleanField(default=False)

    class Meta:
        ordering = ['-admitted_on']
    
    def __str__(self):
        return self.name
