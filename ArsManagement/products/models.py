from django.db import models

class Casing(models.Model):
    product_name = models.CharField(max_length=255)
    product_model = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)  # Slug is often unique to avoid URL conflicts
    date = models.DateField(auto_now_add=True)  # Automatically adds the date when created
    image = models.ImageField(upload_to='casings/', default='fallback.png', blank=True)

    def __str__(self):
        return self.product_name
    

class Gpu(models.Model):
    product_name = models.CharField(max_length=255)
    product_model = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)  # Slug is often unique to avoid URL conflicts
    date = models.DateField(auto_now_add=True)  # Automatically adds the date when created
    image = models.ImageField(upload_to='Gpu/', default='fallback.png', blank=True)

    def __str__(self):
        return self.product_name
