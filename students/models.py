from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
