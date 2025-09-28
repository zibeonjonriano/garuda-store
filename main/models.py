from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothes', 'Clothes'),
        ('jersey', 'Jersey'),
        ('accessory', 'Accessory'),
        ('shoes', 'Shoes'),
        ('merchandise', 'Merchandise'),
    ]

    SIZE_CHOICES = [
        ('xs','XS'),
        ('s','S'),
        ('m','M'),
        ('l','L'),
        ('xl','XL')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini

    #atribut wajib 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category =  models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='no category')
    is_featured = models.BooleanField(default=False)
    

    #atribut opsional
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='xs')      # S, M, L, XL
    stock = models.IntegerField(default=0)

    product_views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.name} - ({self.category})"
    #itu fungsinya buat nge-representasikan object Product jadi string yang lebih gampang dibaca.

    @property
    def is_product_hot(self):
        return self.product_views > 20
            
    def increment_views(self):
        self.product_views += 1
        self.save()