from django.db import models


class Collection(models.Model):

    class PaymentMode(models.TextChoices):
        CASH = "CASH", "Cash"
        UPI = "UPI", "UPI"
    class PaymentStatus(models.TextChoices):
        PAID = "PAID", "Paid"
        UNPAID = "UNPAID", "Unpaid"    
        
    person_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    collection_date = models.DateField()
    payment_mode = models.CharField(
        max_length=10,
        choices=PaymentMode.choices
    )
    token = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )
    collector_name = models.CharField(max_length=100)
    payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
    )
    date = models.DateTimeField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return f"{self.person_name} - {self.amount}"

    def token_number(self):
        return f"{self.collection_date.strftime('%Y')}-{self.id}"