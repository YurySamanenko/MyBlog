from django.db import models
from django.urls import reverse

from blog.misc import RATING_TYPE, OK


class Topic(models.Model):
    name = models.CharField(max_length=255, default="", null=False, blank=False)
    title = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.name}-{self.id}"

    @staticmethod
    def get_absolute_url():
        return reverse('topics', args='')


class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=255)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}-{self.id}"

    @staticmethod
    def get_absolute_url():
        return reverse('topics', args='')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_TYPE, default=OK)

    def __str__(self):
        return '%s - %s' % (self.post.topic, self.text)

    @staticmethod
    def get_absolute_url():
        return reverse('topics', args='')
