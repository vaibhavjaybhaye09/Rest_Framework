from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(max_length=10)
    time = models.DateTimeField(auto_created=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name