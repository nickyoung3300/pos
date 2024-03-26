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

    
