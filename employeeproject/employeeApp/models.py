from django.db import models

# Create your models here.


class employee(models.Model):
    name=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

# string represent-str representation 
    def _str_(self):
        return self.name