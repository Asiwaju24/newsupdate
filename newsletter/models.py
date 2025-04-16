from django.contrib.auth.models import User
from django.db import models

class Newsletter(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    short_description = models.TextField(max_length=500)
    sender_email = models.EmailField()
    image = models.ImageField(upload_to = "images/", blank=True, null=True)

    def __str__(self):
        return self.title
        
        
class Subscriber(models.Model):
    email = models.EmailField()
    newsletters = models.ManyToManyField(Newsletter, related_name='subscribers')

    def __str__(self):
        return self.email