from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Waters(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    w_name = models.CharField(max_length=100)
    size = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = 'waters'

    def __str__(self):
        return self.w_name
