from django.db import models


# Create your models here.
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


class Product(models.Model):
    prepopulated_fields = {"slug": ("title",)}
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    discount = models.FloatField()
    image = models.ImageField(upload_to='')
    key_features = models.JSONField()
    slug = AutoSlugField(populate_from='name')
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
