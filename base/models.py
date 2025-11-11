from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)


class Country(models.Model):
	name = models.CharField("max_length=250")
	alpha_code2 = models.CharField(max_length=2)
	alpha_code3 = models.CharField(max_length=3)
	numeric_code3 = models.CharField(max_length=3)
	created = models.DateTimeField(auto_now_add=True)