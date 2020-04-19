from django.db import models

# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(default='user', max_length=121)
    email = models.EmailField()
    message = models.TextField()
