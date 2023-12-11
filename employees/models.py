from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
