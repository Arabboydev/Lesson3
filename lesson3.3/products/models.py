from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    model = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    price = models.IntegerField()
    color = models.CharField(max_length=150)
    body = models.TextField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.model


