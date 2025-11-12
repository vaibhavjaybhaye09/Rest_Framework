from django.db import models

# Create your models here.
class Transactions(models.Model):
    TRANSACTIONS_TYPES = [
              ('CREDIT', 'credit'),
              ('DEBIT', 'debit')
        ]
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    Transactions_type = models.CharField(max_length=100, choices=TRANSACTIONS_TYPES)

    def save(self,*args, **kwargs):
        if self.Transactions_type == "DEBIT":
            self.amount == self.amount *- 1
        return super.save()