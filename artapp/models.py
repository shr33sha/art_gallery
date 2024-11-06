# artapp/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=50)
    art = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="artworks")
    blockbuster = models.BooleanField(default=False)  # Flag for "2024 Art Blockbuster" section

    def __str__(self):
        return f"{self.name} - {self.art}"
