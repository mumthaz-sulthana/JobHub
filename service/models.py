from django.db import models

# Create your models here.

class Customer(models.Model):
    
    name=models.CharField(max_length=200)
    
    phone=models.CharField(max_length=200)
    
    email=models.CharField(max_length=200)
    
    vehicle_number=models.CharField(max_length=200)
    
    running_kilometer=models.IntegerField()
    
    work_choices=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("completed","completed")
    )
    
    work_status=models.CharField(max_length=200,choices=work_choices,default="pending")
    
    
class Work(models.Model):
    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    description=models.TextField()
    
    amount=models.FloatField()