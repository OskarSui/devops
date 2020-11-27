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

# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(default=timezone.now)
#     content = models.TextField()
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     status = models.BooleanField(default=True)
#
#     def str(self):
#         return self.user.username

# class Tag(models.Model):
#     title = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=50, unique=True)
#
#     def __str__(self):
#         return '{}'.format(self.title)






