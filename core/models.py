from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Courier(models.Model):
    name = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DeliveryOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
