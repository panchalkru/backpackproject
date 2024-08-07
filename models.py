from django.db import models

# Create your models here.

class Information(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    comment=models.CharField(max_length=50)
    
    def __str__(self):
        return self.firstname

class shop(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField(upload_to="image")

    def __str__(self):
        return self.name

class sign(models.Model):
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)

    def __str__(self):
        return self.uname
    

class CartProduct(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField(upload_to="image")
    quantity=models.CharField(max_length=10,default=1)
    subtotal=models.CharField(max_length=10,default=50)

    def __str__(self):
        return self.name

