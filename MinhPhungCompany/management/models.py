from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    lastname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64, null=True)
    firstname = models.CharField(max_length=64)
    phone = models.CharField(max_length=64, null=True)
    socialnumber = models.IntegerField(null=True)
    customer_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.lastname} {self.middlename} {self.firstname}'


class Product(models.Model):
    measurement_unit_choices = [
        ('m', 'meter'),
        ('y', 'yard'),
    ]

    product_id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=64)
    hexcolor = models.CharField(max_length=64)
    length = models.FloatField()
    measurement_unit = models.CharField(max_length = 64, choices = measurement_unit_choices)
    type = models.CharField(max_length=64)
    location = models.CharField(max_length=64, null=True)
    measurement_unit = models.CharField(max_length=64, choices=measurement_unit_choices)
    product_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.type} / {self.color} / {self.length}'


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.customer}-{self.product}'
