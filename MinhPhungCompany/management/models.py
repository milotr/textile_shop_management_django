from django.db import models

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    socialnumber = models.IntegerField(null=True)
    customer_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Type(models.Model):
    type_id = models.BigAutoField(primary_key=True)
    typeOfProduct = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.typeOfProduct}'

class Color (models.Model):
    color_id = models.BigAutoField(primary_key=True)
    typeKey = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    colorOfType = models.CharField(max_length=64)
    def __str__(self):
        return f'{self.typeKey} - {self.colorOfType}'
class Roll(models.Model):
    roll_id = models.BigAutoField(primary_key=True)
    colorKey = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    length = models.FloatField()
    measurement_unit_choices = [
        ('m', 'meter'),
        ('y', 'yard'),
    ]
    measurement_unit = models.CharField(max_length = 64, choices = measurement_unit_choices)
    location = models.CharField(max_length=64, null=True)
    roll_date = models.DateTimeField(auto_now_add=True, null=True)
    sold = models.BooleanField()
    def __str__(self):
        return f'{self.length}{self.measurement_unit}'


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    roll = models.ForeignKey(Roll, null=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    delivery_choices = [
        ('Đã giao', 'Đã giao'),
        ('Chưa giao', 'Chưa giao'),
        ('Đang giao', 'Đang giao'),
    ]
    delivery = models.CharField(max_length=64, choices=delivery_choices)
    deliverer = models.CharField(max_length=64)
    payment_choices = [
        ('Chưa thanh toán', 'Chưa thanh toán'),
        ('Đã thanh toán', 'Đã thanh toán'),
    ]
    payment = models.CharField(max_length=64, choices=payment_choices)

    def __str__(self):
        return f'{self.customer}-{self.product}'
