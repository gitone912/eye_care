from django.db import models

# Create your models here.
selection = (
    ('m', 'male'),
    ('f', 'female'),
    )
class user_details(models.Model):
    name = models.CharField(max_length=60, blank=True, default='',verbose_name="name" )
    age = models.IntegerField(blank=True, default='',verbose_name="age" )
    gender = models.CharField(max_length=60, blank=True, default='',choices=selection,verbose_name="status" )
    mail_id = models.EmailField(max_length=60, blank=True, default='',verbose_name="mail_id" )
    image1 = models.ImageField(upload_to='images/', blank=True, default='',verbose_name="images" )
    image2 = models.ImageField(upload_to='images/', blank=True, default='',verbose_name="images" )
    