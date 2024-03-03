from audioop import reverse
from django.db import models

class Authors_public(models.Model):
    name = models.CharField(max_length=15, blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    

class BoardManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().all()


class Public_board(models.Model):
    title = models.CharField(max_length=15, blank=True)
    date_public_boards = models.DateField()
    auto_public = models.BooleanField()
    content = models.TextField()
    interest = models.BooleanField()
    
    
    
    def __str__(self) -> str:
        return f'{self.title}'
    
    def get_absolute_url(self):
       return reverse(" Public_board", kwargs={"pk": self.pk})
    
    
    

class Relevance_board(models.Model):
    title = models.CharField(max_length=45, blank=True)
    themes = models.TextField()
    dates = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return  f'{self.title}'
    
    
class Username(models.Model):
    name = models.CharField(max_length=15, blank=True)
    phone = models.IntegerField()
    
    
    
    
    
      
    