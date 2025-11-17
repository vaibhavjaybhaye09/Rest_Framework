from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    completed = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updcated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at'] 
    
    def __str__(self):
        return self.title