from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    
class Expense(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=100)
    receipt = models.ImageField(upload_to="receipts/",blank=True,null=True)
    
    def __str__(self):
        return self.title