from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    class Meta:
        ordering = ['name']  # ✅ alphabetical order

    def __str__(self):
        return f"{self.name} (${self.price})"
