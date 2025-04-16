from django.db import models
from datetime import datetime


class Category(models.Model):
	name = models.CharField(max_length = 50)
	
	def __str__ (self):
		return self.name
		
		
	class Meta:
		verbose_name_plural='categories'

class Post(models.Model):
	title = models.CharField(max_length= 100, default="Title")
	body = models.TextField(max_length = 10000, default ="Content")
	created_at = models.DateTimeField(default= datetime.now, blank= True)
	image = models.ImageField(null = True, blank = True, upload_to = "images/")
	author = models.CharField(max_length= 100, default= "Author Name")
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	trending = models.BooleanField(default = False)