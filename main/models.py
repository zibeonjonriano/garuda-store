from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini

    #atribut wajib 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    #atribut opsional
    size = models.CharField(max_length=20, blank=True)      # S, M, L, XL
    stock = models.IntegerField(default=0)


def __str__(self):
    return f"{self.name} ({self.team})"
#itu fungsinya buat nge-representasikan object Product jadi string yang lebih gampang dibaca.