from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from django import forms
from django.forms import ModelForm

# Create your models here.
class catagory(models.Model):
	product_catg = models.CharField(max_length=200)

	def __unicode__(self):
		return self.product_catg

class Product(models.Model):
	product_type = models.ForeignKey(catagory)
	product_name = models.CharField(max_length=200)
	product_brand = models.CharField(max_length=200)
	product_price = models.IntegerField(default=0)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	cart_value= models.BooleanField(default=False)
	product_pic=models.FileField("product_pic",upload_to="trialshop/static/media/%Y/%m/%d",blank=True,null=True)
	product_pic_name=models.CharField(max_length=100)
	product_detail=models.TextField()
	list_display = ["product_name", "product_brand", "product_price", "pub_date", "cart_value","thumbnail"]
	
	def __unicode__(self):
		return self.product_name

class Cart(models.Model):
	user=models.ForeignKey(User)
	product_id=models.ForeignKey(Product)
	pid=models.IntegerField(default=0)
	quantity=models.IntegerField(default=1)
	price=models.IntegerField(default=0)
	product_pic=models.CharField(max_length=200)
	product_name = models.CharField(max_length=200)
	product_brand = models.CharField(max_length=200)
	product_type = models.CharField(max_length=200)
	product_detail=models.TextField()
	total_val=models.IntegerField(default=0)
	def __unicode__(self):
		return self.product_brand
