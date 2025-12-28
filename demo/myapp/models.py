from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200) # python attribute - properties of the db
    completed = models.BooleanField(default=False)

class WhatsAppItem(models.Model):
    name = models.CharField(max_length=200) # python attribute - properties of the db
    phoneNumber = models.CharField(max_length=200)
    emailAddress = models.CharField(max_length=200)  