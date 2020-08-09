from django.db import models
from posts.models import User, Post


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                   editable=False,
                                   verbose_name='Post')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                   editable=False,
                                   verbose_name='User')

    def __str__(self):
        return '%s upvote %s' % (self.user.id, self.post.id)
