from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
         return self.name
