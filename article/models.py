from django.db import models
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(unique=True, max_length=37)

    def __str__(self):
        return self.name


ARTICLE_TYPE_CHOICE = [
    ('MR', 'Must Read'),
    ('RS', 'Read Slowly'),
    ('FF', 'Fun Fact'),
]

class Post(models.Model):
    title = models.CharField(max_length=121, default='Title')
    published = models.DateField(default=timezone.now)
    kind_post = models.CharField(max_length=2, default='MR', choices=ARTICLE_TYPE_CHOICE)

    def __str__(self):
        return self.title


