from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
    ]
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.title} - {self.transaction_type} - ₹{self.amount}"
