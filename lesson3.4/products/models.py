from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Student(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student/',blank=True, null=True)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    age = models.IntegerField()
    region = models.CharField(max_length=255)
    university = models.CharField(max_length=255)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return f"{self.f_name}"
