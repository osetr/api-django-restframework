from django.db import models
from users.models import User
from django.core.validators import (
    MaxValueValidator, MinValueValidator)
from datetime import datetime


class Post(models.Model):
    min_value = MinValueValidator(1)
    max_value = MaxValueValidator(250)
    title = models.CharField(verbose_name='Title', max_length=25)
    date = models.DateTimeField(default=datetime.now(),
                                editable=False)
    content = models.TextField(verbose_name='Content',
                               default='no content',
                               max_length=250)
    author = models.CharField(verbose_name='Author',
                              editable=False,
                              max_length=25)
    upvotes = models.IntegerField(verbose_name='Upvotes', default=0)
    user = models.ForeignKey(User, verbose_name='User',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return '%s by %s' % (self.title, self.author)
