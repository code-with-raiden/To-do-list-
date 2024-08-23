from django.db import models

# Create your models here.
class To_do(models.Model):
    new_task = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.new_task
    
class History(models.Model):
    new_task = models.CharField(max_length=50)
    desc = models.TextField()
    def __str__(self):
        return self.new_task    