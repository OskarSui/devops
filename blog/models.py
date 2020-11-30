from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField()
    # tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)








