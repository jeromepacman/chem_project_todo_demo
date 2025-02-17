from django.db import models
from django.contrib.auth.models import User

from apps.store.models import Product


class Order(models.Model):
    ORDERED='pending'
    PROCESS='in process'
    SHIPPED='shipped'
    CANCELLED='cancelled'

    STATUS_CHOICES=[
        (ORDERED, 'Pending'),
        (PROCESS, 'In process'),
        (SHIPPED, 'Shipped'),
        (CANCELLED, 'Cancelled')
    ]

    user=models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    zipcode=models.CharField(max_length=20)
    place=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)

    created_at=models.DateTimeField(auto_now_add=True)

    paid=models.BooleanField(default=False)
    paid_amount=models.FloatField(blank=True, null=True)
    used_coupon=models.CharField(max_length=20, blank=True, null=True)

    payment_intent=models.CharField(max_length=200)

    shipped_date=models.DateTimeField(blank=True, null=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default=ORDERED)

    def __str__(self):
        return '%s' % self.first_name

    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())


class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
    price=models.FloatField()
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
