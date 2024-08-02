from django.db import models

# Create your models here.
class Employee(models.Model):
    matricule = models.CharField(max_length=30 , primary_key=True , null=False)
    last_name = models.CharField(max_length=30 ,null=False)
    first_name = models.CharField(max_length=30 , null=False)
    salary = models.FloatField(null=False)

    def __str__(self):
        return f"{self.matricule} {self.last_name} {self.first_name} {self.salary}"


class Payements(models.Model):
    id = models.AutoField(primary_key=True )
    matricule = models.ForeignKey(Employee , on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField(null=False)

    def __str__(self):
        return f"{self.matricule.matricule}  {self.date} { self.amount}"
    