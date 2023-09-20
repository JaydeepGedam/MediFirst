from django.db import models
import datetime
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    frontimg = models.ImageField(upload_to='product/images/frontimg', default="")
    img1 = models.ImageField(upload_to='product/images/img1')
    img2 = models.ImageField(upload_to='product/images/img2')
    img3 = models.ImageField(upload_to='product/images/img3')
    img4 = models.ImageField(upload_to='product/images/img4')
    prod_name = models.CharField(max_length=100, unique=True)
    prod_price = models.FloatField()
    prod_detail = models.CharField(max_length=300)
    prod_content = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(username):
        return Order.objects.filter(username=username).order_by('-date')
        

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    msg = models.CharField(max_length=500)

class Appointment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    aptdate = models.DateField(default=datetime.datetime.today)
    tddate = models.DateField(default=datetime.datetime.today)
    selectdoctor = models.CharField(max_length=200)
    msg = models.CharField(max_length=500)
    status = models.BooleanField(default=False)

class Donate(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    dnr_name = models.CharField(max_length=200)
    dnr_address = models.CharField(max_length=200)
    dnr_phone = models.CharField(max_length=10)
    drg_name = models.CharField(max_length=100)
    drg_lotno = models.CharField(max_length=20)
    drg_exdate = models.DateField(default=datetime.datetime.today)
    drg_quantity = models.IntegerField()
    drg_strength = models.CharField(max_length=10)
    signature = models.ImageField(upload_to='signatures')
    today_date = models.DateField(default=datetime.datetime.today)




class Admin_Register(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField('password', max_length=50, validators=[MinLengthValidator(8)])
    group = models.CharField(max_length=30,default='admin', blank=True)

class Doctor_Register(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField('password', max_length=50, validators=[MinLengthValidator(8)])
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    group = models.CharField(max_length=30,default='doctor', blank=True)

class User_Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='profile_photos', default="profile_phots/default.jpg")
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)




    



