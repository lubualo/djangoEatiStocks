import datetime
from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.ticker}"


class Investment(models.Model):
    date = models.DateField(
        default=datetime.date.today, auto_now=False, auto_now_add=False
    )
    quantity = models.FloatField()
    pricePerUnit = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def getTotal(self):
        return self.quantity * self.pricePerUnit

    def __str__(self):
        return f"{self.stock} - Amount: {self.quantity} - Total: {self.getTotal():.2f}"
