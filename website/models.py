from django.db import models
from django.utils import timezone
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    #publish_date = models.DateField(default = timezone.now)
    publish_date = models.DateField(default = date.today)
    in_stock = models.BooleanField(default=True)

    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title, self.author, self.publish_date, self.in_stock
