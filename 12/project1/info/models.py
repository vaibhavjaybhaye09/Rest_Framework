from django.db import models

# Create your models here.
class Student(models.Model):
    STAUS_CHOICE = [
        'pass','PASS',
        'fail','FAIL'
    ]
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    marks = models.IntegerField(null=True)
    status = models.Choices(STAUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def  __str__(self):
        return self.name