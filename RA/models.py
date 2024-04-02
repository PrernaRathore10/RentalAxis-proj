from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=255, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    img=models.ImageField(upload_to="Static\product_img", default="")

    def __str__(self):
        return self.product_name

class member(models.Model):
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    phone_number = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)