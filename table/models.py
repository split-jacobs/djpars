from django.db import models

class Table(models.Model):
	title = models.CharField(max_length = 50)
	link = models.URLField()
	name = models.CharField(max_length = 30)
	number =models.CharField(max_length = 25)
	email = models.EmailField()
	address = models.CharField(max_length = 50)
	date_public = models.CharField(max_length=30)
	
