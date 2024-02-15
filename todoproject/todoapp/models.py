from django.db import models
class TodoListItem(models.Model):
    content = models.TextField() 
    completed=models.BooleanField()

# Create your models here.
