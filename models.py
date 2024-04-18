from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length = 50)

class Employee(models.Model):
    fullname = models.CharField(max_length = 100)
    emp_code = models.CharField(max_length = 3)
    mobile = models.CharField(max_length = 15)
    position = models.ForeignKey(Position, on_delete = models.CASCADE)


class Category(models.Model):
    categoryname = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryname

class Menu(models.Model):
    product = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # 添加 total_price 字段来保存订单的总金额
    # 其他订单信息

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    suger = models.CharField(max_length=100)
    temp = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total_price(self):
        return int(self.unit_price) * int(self.quantity)
