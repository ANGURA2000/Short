# from django.db import models

# Create your models here.

# class Contact(models.Model):
#     Name= models.CharField(max_length=255)
#     Email= models.EmailField(max_length=255)
#     Message= models.CharField(max_length=500)

#     def __str__(self):
#         return self.Name

# models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name} - {self.email}"
    
class ReportMessage(models.Model):
    invalidmal = models.CharField(max_length=50)
    comment = models.TextField(max_length=100)
    def __str__(self):
        return f"{self.invalidmal}"   
    

# main/models.py
from django.db import models
import random
import string

class ShortURL(models.Model):
    short_key = models.CharField(max_length=10, unique=True)
    long_url = models.URLField()

    @classmethod
    def create_short_url(cls, long_url):
        short_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        short_url = cls.objects.create(short_key=short_key, long_url=long_url)
        return short_url

    @classmethod
    def get_long_url(cls, short_key):
        try:
            short_url = cls.objects.get(short_key=short_key)
            return short_url.long_url
        except cls.DoesNotExist:
            return None

