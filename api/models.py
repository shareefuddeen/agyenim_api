from django.db import models
from cloudinary.models import CloudinaryField

class Announcement(models.Model):
    title = models.CharField(null= False,blank=False , max_length=50)
    content = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
    

class Faqs(models.Model):
    question = models.TextField(null=False,blank=False)
    answer = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'question {self.id}'
    

class Contact(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    email =models.CharField(max_length=60,blank=False,null=False)
    phone_number = models.BigIntegerField(blank=False,null=False)
    message = models.TextField(blank=False,null=False)
    
    
    def __str__(self):
        return f'message by {self.name}'


class Blog(models.Model):
    title = models.CharField(max_length=66, null=False,blank=False)
    content = models.TextField(null=False,blank=False)
    image = CloudinaryField('image', blank=True, null=True)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Team(models.Model):
    name =models.CharField(max_length=50,null=False,blank=False)
    title = models.CharField(max_length=40,null=False,blank=False)
    description = models.CharField(max_length=160,null=False,blank=False)
    image = CloudinaryField('image', blank=True, null=True)

    
    def __str__(self):
        return f'{self.name} ({self.title})'
    