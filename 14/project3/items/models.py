from django.db import models

# Create your models here.
class Items(models.Model):
    size = models.BigIntegerField(auto_created=True)
    product = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.product