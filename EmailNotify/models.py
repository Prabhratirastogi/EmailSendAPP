from django.db import models

# Create your models here.
class PantryItem(models.Model):
    name = models.CharField(max_length = 100)
    description =  models.TextField()
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return self.name
    

class PantryOrder(models.Model):
    order_date = models.DateField(auto_now_add=True)
    item = models.ForeignKey(PantryItem,on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id} ({self.order_date})"