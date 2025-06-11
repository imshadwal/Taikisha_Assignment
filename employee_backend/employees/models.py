from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True)
    photo = models.ImageField(upload_to='employee_photos/')
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

    class Meta:
        ordering = ['name']
