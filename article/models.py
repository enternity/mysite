from django.db import models
from django.shortcuts import reverse
import datetime
from django.utils.text import slugify
class Topic(models.Model):
    name = models.CharField(unique=True, max_length=37)

    def __str__(self):
        return self.name


ARTICLE_TYPE_CHOICE = [
    ('MR', 'Must Read'),
    ('RS', 'Read Slowly'),
    ('FF', 'Fun Fact'),
]

class Article(models.Model):
    title = models.CharField(max_length=121, default='Title')
    slug = models.SlugField(unique=True)
    published = models.DateField(default=datetime.date.today)
    kind_article = models.CharField(max_length=2, default='MR', choices=ARTICLE_TYPE_CHOICE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article,self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={'id': self.pk, 'slug': self.slug})
    
