from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Technology(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    body = models.TextField(max_length=100)

    class Meta:
        db_table = 'computers'

    def __str__(self):
        return f"{self.category.name} {self.model}"
