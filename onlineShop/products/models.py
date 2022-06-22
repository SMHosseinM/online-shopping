from django.db import models

# Create your models here.


class Category(models.Model):
    GENDER = [('M', 'Male'), ('F', 'Female')]
    title = models.CharField(max_length=30)
    sex = models.CharField(
        max_length=1,
        choices=GENDER,
    )


class Product(models.Model):
    title = models.CharField(max_length=30)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images')


class ProductInventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    size = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    deleted_at = models.DateTimeField()


